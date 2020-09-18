from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from broker.utils.verification.verification import check_phone, clean_phone
from clients.utils.decorators import client_or_none_only, client_only
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
                try:
                    client = User.objects.get(phone=phone)
                    auth_otp = get_otp_code()
                    request.session["auth_otp"] = auth_otp
                    request.session["auth_phone"] = phone
                    request.session["auth_step"] = second
                    request.session.modified = True
                    state = {"phone": True, "phone_editable": False,
                             "otp": True, "otp_editable": False,
                             "password": True, "password_editable": True}
                    parameters = {"otp_code": auth_otp}
                    return Response({"state": state, "parameters": parameters}, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    pass
            else:
                errors = {"message": "Вкажіть новер телефону вірно"}
                state = {"phone": True, "phone_editable": True}
                return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)
        else:
            errors = {"message": "Будь ласка введіть номер телефону"}
            state = {"phone": True, "phone_editable": True}
            return Response({"errors": errors, "state": state}, status=status.HTTP_200_OK)
    elif auth_step == second:
        pass
    else:
        pass
    return Response({}, status=status.HTTP_200_OK)


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
