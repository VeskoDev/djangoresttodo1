
from todos.views import TodosAPIView, TodoDetailAPIView
from django.urls import path 

# CreateTodoApiView, TodoListAPIView,


urlpatterns = [     
    path("", TodosAPIView.as_view(), name="todos"),
    path("<int:id>", TodoDetailAPIView.as_view(), name="todo")
    # path('create', CreateTodoApiView.as_view(), name="create-todo"),
    # path('list', TodoListAPIView.as_view(), name="list-todos"),
]