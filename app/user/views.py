from django.contrib.auth import authenticate, login

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(CreateAPIView):
    """
    API endpoint to register a new user.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    """
    API endpoint for user login, returns authentication token.
    """
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        """
        Handle POST request to authenticate a user and return a token.
        """
        # username = request.data.get('username')
        # password = request.data.get('password')
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK, )
            else:
                return Response({'detail': 'User account is not active'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
