import graphene
from type import User
from data import users

class CreateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, name, email, password):
        user = User(id=id, name=name, email=email, password=password)
        users.append({
            "id": id,
            "name": name,
            "email": email,
            "password": password
        })
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, name=None, email=None, password=None):
        # Find the existing user by ID
        old_user = next((user for user in users if user["id"] == id), None)
        
        if old_user is None:
            raise Exception("User not found")

        # Update user details if provided
        if name:
            old_user["name"] = name
        if email:
            old_user["email"] = email
        if password:
            old_user["password"] = password

        return UpdateUser(user=User(id=old_user["id"], name=old_user["name"], email=old_user["email"], password=old_user["password"]))


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(root, info, id):
        # Find the existing user by ID
        old_user = next((user for user in users if user["id"] == id), None)
        
        if old_user is None:
            raise Exception("User not found")

        # Remove the user from the list
        users.remove(old_user)

        return DeleteUser(user=User(id=old_user["id"], name=old_user["name"], email=old_user["email"], password=old_user["password"]))


# Example of a Mutation class that includes these mutations
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
