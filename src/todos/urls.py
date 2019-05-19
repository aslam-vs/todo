from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('todos/', views.TodosView.as_view(), name='todos'),
    path('todos/<int:pk>/', views.DetailsView.as_view(), name='view_todo'),
    path('todos/add/', views.CreateView.as_view(), name='add_todo'),
    path('todos/add/<int:pk>/', views.CreateView.as_view(), name='edit_todo'),


    path('app/v1/todos/', views.ToDoApiView.as_view(), name='api_todos'),
    path('app/v1/todos/<int:pk>/', views.ToDoApiView.as_view(), name='api_todos'),

]