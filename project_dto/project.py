import graphene
from django.contrib.auth.models import User
from myapp.models import *


# class RegisterUserInputObject(graphene.InputObjectType):
#     username = graphene.String()
#     email = graphene.String()
#     first_name = graphene.String()
#     last_name = graphene.String()
#     password = graphene.String()
    
# class RegisterUserObject(graphene.ObjectType):
#     username = graphene.String()
#     email = graphene.String()
#     first_name = graphene.String()
#     last_name = graphene.String()
#     is_active =graphene.Boolean()

from graphene import InputObjectType
class UserRegistrationInputObject(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()
    password_confirm = graphene.String()
    
class UserRegistrationObject(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    
class UserLoginInputObject(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()
    
class UserLoginObject(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    refresh_token = graphene.String()
    access_token = graphene.String()
    