from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

User = settings.AUTH_USER_MODEL


@api_view(['POST'])
def client_sign_in(request):
    """ Client SignIn """
    if request.method == 'POST':

        return Response(status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def client_sign_up(request):
    """ Client SignUp """
    if request.method == 'POST':

        return Response(status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
