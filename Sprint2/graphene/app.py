import graphene
from mutation import DeleteUser, UpdateUser, CreateUser
from query import Query
from type import User

# Mutation definitions
class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

# Query definitions
class MyQuery(Query):
    # Get a single user by ID
    user = graphene.Field(User, id=graphene.String(required=True))
    
    # Get a list of users
    all_users = graphene.List(User)

    def resolve_user(self, info, id):
        # Assuming you have logic to get a user by ID
        pass
    
    def resolve_all_users(self, info):
        # Assuming you have logic to get all users
        pass

# Create the schema
schema = graphene.Schema(query=MyQuery, mutation=MyMutations)

# Mutation to create User 2
result_create = schema.execute(
    '''
    mutation {
        createUser(id: "2", name: "SecondUser", email: "seconduser@email.com", password: "abcdefg") {
            user {
                id
                name
                email
                password
            }
        }
    }
    '''
)

# Mutation to update User 2
result_update = schema.execute(
    '''
    mutation {
        updateUser(id: "2", name: "UpdatedSecondUser", email: "updatedseconduser@email.com", password: "newpassword") {
            user {
                id
                name
                email
                password
            }
        }
    }
    '''
)

# Mutation to delete User 2
result_delete = schema.execute(
    '''
    mutation {
        deleteUser(id: "2") {
            success
            message
        }
    }
    '''
)

# Print the results of all operations
print("Create User 2 Result: ", result_create.data)
print("Update User 2 Result: ", result_update.data)
print("Delete User 2 Result: ", result_delete.data)
