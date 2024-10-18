import graphene
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken




# User = get_user_model()

# class RegisterUserBuilders:
#     @staticmethod
#     def get_user_data(id=None):
#         # Fetch data by unique ID
#         if id:
#             user = User.objects.filter(id=id).first()
#             if user:
#                 return RegisterUserObject(
#                     id=user.id,
#                     username=user.username,
#                     email=user.email,
#                     first_name=user.first_name,
#                     last_name=user.last_name,
#                     is_active=user.is_active,
#                 )
#         return None

class UserBuilder:
    @staticmethod
    def register_user(username, email, password, password_confirm):
        if password != password_confirm:
            raise ValidationError("Password do not match")
        
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
    
    @staticmethod
    def login_user(username, password):
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Invalid username or password')
        
        # Create tokens for the authenticated user
        refresh = RefreshToken.for_user(user)
        return {
            'user': user,
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }