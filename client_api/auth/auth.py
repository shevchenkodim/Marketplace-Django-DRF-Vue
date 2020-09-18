from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from clients.utils.decorators import client_or_none_only, client_only
from common.models import User
from broker.utils.otp_code.otp_code import GenerateOtpCode


@api_view(['POST'])
@client_or_none_only
def client_auth(request):
    """ Client Auth """
    if request.method == 'POST':

        return Response({}, status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


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
