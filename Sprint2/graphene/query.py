from graphene import ObjectType
from data import users
class Query(ObjectType):
    def resolve_get_user(root, info , id):
        return list(filter(lambda user: user["id"]==id)[0])
    
    def resolve_get_user(root , info):
        return users