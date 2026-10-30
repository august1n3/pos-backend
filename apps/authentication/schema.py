import graphene
from apps.authentication.mutations import Mutations
from apps.authentication.quaries import POSUserQuery
schema = graphene.Schema(mutation=Mutations, query=POSUserQuery)
