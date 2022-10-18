from django.urls import path


from todo.views import TaskListView, TagListView, TagUpdateView, TagDeleteView, TaskUpdateView, TaskDeleteView, \
    task_complete_view, TaskCreateView, TagCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/complite/<int:pk>", task_complete_view, name="task-complete"),
]

app_name = "todo"
