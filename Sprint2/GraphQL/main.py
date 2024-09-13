from flask import Flask, request, jsonify
from graphene import ObjectType, String, Int, Field, Mutation, Schema, List
from graphene import InputObjectType
from flask_graphql import GraphQLView


tasks = []

class TaskType(ObjectType):
    id = Int()
    task = String()
    date = String()
    status = String()

# Input type for task creation and updates
class TaskInput(InputObjectType):
    task = String(required=True)
    date = String(required=True)
    status = String(required=True)

# Create Task Mutation
class CreateTask(Mutation):
    class Arguments:
        input = TaskInput(required=True)
    
    task = Field(lambda: TaskType)

    def mutate(root, info, input):
        task_id = len(tasks) + 1
        task_data = {
            'id': task_id,
            'task': input.task,
            'date': input.date,
            'status': input.status
        }
        tasks.append(task_data)
        return CreateTask(task=task_data)

# Update Task Mutation
class UpdateTask(Mutation):
    class Arguments:
        id = Int(required=True)
        input = TaskInput(required=False)

    task = Field(lambda: TaskType)

    def mutate(root, info, id, input):
        for task in tasks:
            if task['id'] == id:
                task['task'] = input.task if input.task else task['task']
                task['date'] = input.date if input.date else task['date']
                task['status'] = input.status if input.status else task['status']
                return UpdateTask(task=task)
        return None

# Delete Task Mutation
class DeleteTask(Mutation):
    class Arguments:
        id = Int(required=True)

    task = Field(lambda: TaskType)

    def mutate(root, info, id):
        global tasks
        for task in tasks:
            if task['id'] == id:
                tasks = [t for t in tasks if t['id'] != id]
                return DeleteTask(task=task)
        return None

# Query to get a single task by ID
class Query(ObjectType):
    get_task = Field(TaskType, id=Int(required=True))

    def resolve_get_task(root, info, id):
        for task in tasks:
            if task['id'] == id:
                return task
        return None


class Mutation(ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()


schema = Schema(query=Query, mutation=Mutation)


app = Flask(__name__)


app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the GraphQL API for Tasks!"})

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
