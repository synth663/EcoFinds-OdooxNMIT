from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from .models import CustomUser

class RegisterView(APIView):
    """
    Handles POST requests to create a new user.
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # This calls the .create() method in our serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Handles POST requests to authenticate and log in a user.
    """
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        # Find the user by their email to get their actual username
        try:
            user_obj = CustomUser.objects.get(email=email)
            # Use Django's built-in authentication with the username and password
            user = authenticate(username=user_obj.username, password=password)

            if user is not None:
                # Login was successful
                return Response({
                    'message': 'Login successful',
                    'username': user.username,
                    # In a real-world app, you would generate and return a secure token here.
                }, status=status.HTTP_200_OK)
            else:
                # Password was incorrect
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except CustomUser.DoesNotExist:
            # No user with the provided email exists
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

