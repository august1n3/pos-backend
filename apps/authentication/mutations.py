import graphene
from graphql import GraphQLError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from apps.authentication.models import POSUser
from apps.authentication.g_types import POSUserType
from django.contrib.auth.decorators import login_required

class CreatePOSUserMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    posUser = graphene.Field(POSUserType)

    
    def mutate(root, info, first_name, last_name, username, email, password):
        try:
            validate_email(email)
        except ValidationError:
            raise GraphQLError("Invalid email was given")

        if len(password) < 8:
            raise GraphQLError("The password is too short 'should be longer than 7 characters'")

        posUser = POSUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role="CASHIER"
        )
        return CreatePOSUserMutation(posUser=posUser)

@login_required
class DeletePOSUserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    
    def mutate(root, info, username, password):
        try:
            user = POSUser.objects.get(username=username)
        except POSUser.DoesNotExist:
            raise GraphQLError("Failed to delete account")

        if not user.check_password(password):
            raise GraphQLError("Failed to delete account")
            
        user.delete()
        return DeletePOSUserMutation(success=True, message="account deleted")

@login_required
class UpdateRolePOSUserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        role = graphene.String(required=True)

    posUser = graphene.Field(POSUserType)

    def mutate(root, info, role, username):
        try:
            user_obj = POSUser.objects.get(username=username)
        except POSUser.DoesNotExist:
            raise GraphQLError("User not found")
            
        user_obj.role = role 
        user_obj.save()      
        
        return UpdateRolePOSUserMutation(posUser=user_obj)

class Mutations(graphene.ObjectType):
    create_p_o_s_user = CreatePOSUserMutation.Field(description="mutation for creating a new POS User")
    update_user_role = UpdateRolePOSUserMutation.Field(description="mutation for changing the role of an existing POS User")
    delete_user = DeletePOSUserMutation.Field(description="deleting an existing user")
