from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from clients.utils.decorators import client_or_none_only, client_only
from common.models import User
from broker.utils.otp_code.otp_code import GenerateOtpCode


@api_view(['POST'])
@client_or_none_only
def client_sign_in(request):
    """ Client SignIn """
    if request.method == 'POST':

        return Response({}, status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@client_or_none_only
def client_sign_up(request):
    """ Client SignUp """
    if request.method == 'POST':

        return Response(status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
