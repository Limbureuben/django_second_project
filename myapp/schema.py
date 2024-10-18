import graphene
from graphene_django.types import DjangoObjectType

from .models import *
from datetime import date
from django.contrib.auth.models import User
from project_dto.project import *
from projectBuilders.projectBuilders import *
from .views import *
import graphql_jwt

        
        
class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    login_user = LoginUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    
class Query(graphene.ObjectType):
    users = graphene.List(UserLoginObject)
    
    def resolve_users(self, info):
        return User.object.all()
    
schema =graphene.Schema(query=Query, mutation=Mutation)
        
    