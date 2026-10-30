from graphene_django import DjangoObjectType
from apps.authentication.models import POSUser
from apps.authentication.g_types import POSUserType
from graphql import GraphQLError
import graphene

class POSUserQuery(graphene.ObjectType):
    user_by_username = graphene.Field(POSUserType, username=graphene.String(),password=graphene.String())
    all_users = graphene.List(POSUserType)

    def resolve_user_by_username(root, info, username, password):
        try:
            user = POSUser.objects.get(username = username)
            if not user.check_password(password):
                Exception()
            return user
        except Exception as e:
            GraphQLError("user is not found")

    def resolve_all_users(root, info):
        user = POSUser.objects.all()
        return user



    

