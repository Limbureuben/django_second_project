import graphene
from graphene_django.types import DjangoObjectType

from myapp.views import CreateRegistrationUserMutation
from .models import *
from datetime import date
from django.contrib.auth.models import User
from project_dto.project import *
from projectBuilders.projectBuilders import *

###let us define the graphql types##


    
    
schema =graphene.Schema()
        
    