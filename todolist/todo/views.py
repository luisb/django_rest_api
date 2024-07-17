from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Todo
# Create your views here.
def todo_list(request):
    """ Return all todos """

    # get all todos
    todos = Todo.objects.all()

    # prepare data to return
    data = {
        'todos': list(todos.values())
    }

    # return JSON
    return JsonResponse(data)

def todo_detail(request, pk):
    """ Return a todo instance """
    try:
        # find todo by id
        todo = Todo.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # return 404 if the todo does not exist
        return JsonResponse({
            'status_code': 404,
            'error': f'Todo with id {pk} not found.'
        })
    else:
        # prepare data to return
        data = {
            'id': todo.id,
            'title': todo.title,
            'completed': todo.completed,
            'user': todo.user.username,
        }

        # return JSON
        return JsonResponse(data)
