from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('todo/list/', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('toggle/<int:pk>/', views.todo_toggle, name='todo_toggle'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('profile/', views.profile, name='profile'),
]
