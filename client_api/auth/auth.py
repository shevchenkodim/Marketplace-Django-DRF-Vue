from django.contrib.auth import login
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from broker.utils.verification.verification import check_phone, clean_phone, check_email
from clients.utils.decorators import client_or_none_only, client_only
from common.access.access import UserRole, AccessRole
from common.geo.user_location_history import UserLocationHistoryModel
from common.models import User
from broker.utils.otp_code.otp_code import GenerateOtpCode

first, second = "FIRST", "SECOND"


@api_view(['POST'])
@client_or_none_only
def client_auth(request):
    """ Client Auth """
    data = request.data
    auth_step = request.session.get("auth_step", first)
    if auth_step == first:
        phone = data.get("phone", None)
        if phone:
            phone = clean_phone(phone)
            if check_phone(phone):
                auth_otp = get_otp_code()
                request.session["auth_otp"] = auth_otp
                request.session["auth_phone"] = phone
                request.session["auth_step"] = second
                request.session.modified = True
                try:
                    client = User.objects.get(phone=phone)
                    state = {"phone": True, "phone_editable": False,
                             "otp": True, "otp_editable": False,
                             "password": True, "password_editable": True}
                    parameters = {"otp_code": auth_otp}
                    return Response({"state": state, "parameters": parameters}, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    state = {"phone": True, "phone_editable": False,
                             "otp": True, "otp_editable": False,
                             "password": True, "password_editable": True,
                             "first_name": True, "first_name_editable": True,
                             "last_name": True, "last_name_editable": True,
                             "email": True, "email_editable": True}
                    parameters = {"otp_code": auth_otp}
                    return Response({"state": state, "parameters": parameters}, status=status.HTTP_200_OK)
            else:
                errors = {"message": "Вкажіть вірний номер телефону"}
                state = {"phone": True, "phone_editable": True}
                return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)
        else:
            errors = {"message": "Будь ласка введіть номер телефону"}
            state = {"phone": True, "phone_editable": True}
            return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)
    elif auth_step == second:
        phone = data.get("phone", None)
        if phone:
            phone = clean_phone(phone)
            session_phone = request.session.get("auth_phone", None)
            if not phone == session_phone:
                errors = {"message": "Підміна телефону"}
                state = {"show_phone": True, "phone_editable": False, "show_otp": False, "step": first}
                return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)

            otp_code = data.get("otp_code")
            session_auth_otp = request.session.get("auth_otp", None)
            if not str(otp_code) == str(session_auth_otp):
                errors = {"message": "Невірній тимчасовий пароль"}
                state = {"show_phone": True, "phone_editable": False, "otp_editable": False,
                         "show_otp": True, "step": second}
                return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)

            try:
                client = User.objects.get(phone=phone)
                password = data.get("password")
                if not client.check_password(password):
                    errors = {"message": "Пароль невірний"}
                    state = {"show_phone": True, "phone_editable": False,
                             "show_otp": True, "otp_editable": False,
                             "show_password": True, "step": second,
                             "password_enabled": True}
                    return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)
                login(request, client)
                try:
                    UserLocationHistoryModel.create_user_location(request=request, user_id=client.id)
                except Exception as e:
                    pass
                return Response({"status": "ok", "redirect": reverse('client:index')}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                first_name = data.get("first_name")
                last_name = data.get("last_name")
                password = data.get("password")
                email = data.get("email")
                if User.has_email(email):
                    errors = {"message": "Такий email вже використовується"}
                    return Response({"errors": errors}, status=status.HTTP_200_OK)
                if not check_email(email):
                    errors = {"message": "Email має невірний формат"}
                    return Response({"errors": errors}, status=status.HTTP_200_OK)
                if not first_name or not last_name:
                    errors = {"message": "Потрібно ввести прізвище та ім'я"}
                    return Response({"errors": errors}, status=status.HTTP_200_OK)
                if not password or len(password) < 8:
                    errors = {"message": "Пароль має бути не менше 8 символів"}
                    return Response({"errors": errors}, status=status.HTTP_200_OK)
                client = User.objects.create_user(
                    email=email,
                    phone=phone,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                )
                UserRole.objects.create(
                    role=AccessRole.objects.get_or_create(role='Клієнт', code_role='client')[0],
                    user=client
                )
                login(request, client)
                try:
                    UserLocationHistoryModel.create_user_location(request=request, user_id=client.id)
                except Exception as e:
                    pass
                return Response({"status": "ok", "redirect": reverse('client:index')}, status=status.HTTP_200_OK)
    else:
        state = {"phone": True, "phone_editable": True}
    return Response({"state": state}, status=status.HTTP_200_OK)


def get_otp_code():
    """ Generate OTP-code for auth client """
    otp_code = GenerateOtpCode.get_random()
    print('OTP-code: ', otp_code)
    return otp_code


@api_view(['GET', 'POST'])
def client_auth_init(request):
    """ Client auth delete session data """
    if request.session.get("auth_phone"):
        del request.session["auth_phone"]
    if request.session.get("auth_email"):
        del request.session["auth_email"]
    if request.session.get("auth_otp"):
        del request.session["auth_otp"]
    if request.session.get("auth_step"):
        del request.session["auth_step"]
    request.session.modified = True
    return Response({}, status=status.HTTP_200_OK)
