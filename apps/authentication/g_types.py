from graphene_django import DjangoObjectType
from apps.authentication.models import POSUser

class POSUserType(DjangoObjectType):
    class Meta:
        model = POSUser
        fields = ("username", "email", "first_name", "last_name", "role")
