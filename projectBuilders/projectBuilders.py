import graphene
from project_dto.project import RegisterUserObject
from django.contrib.auth import get_user_model
from myapp.models import *



User = get_user_model()

class RegisterUserBuilders:
    @staticmethod
    def get_user_data(id=None):
        # Fetch data by unique ID
        if id:
            user = User.objects.filter(id=id).first()
            if user:
                # Return user type object
                return RegisterUserObject(
                    id=user.id,
                    username=user.username,
                    email=user.email,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    is_active=user.is_active,  # Include is_active if needed
                )
        return None  # Return None if user not found or id is not provided
