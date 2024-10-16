import graphene
from django.contrib.auth.models import User
from myapp.models import *





class RegisterUserInputObject(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    password = graphene.String()
    
class RegisterUserObject(graphene.ObjectType):
    username = graphene.String()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    is_active =graphene.Boolean()