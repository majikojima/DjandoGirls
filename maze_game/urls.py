from django.urls import path
from . import views

urlpatterns = [
    path('create_maze/', views.create_maze, name='create_maze'),
    path('move_player/', views.move_player, name='move_player'),
    path('check_status/', views.check_status, name='check_status'),
]
