from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='movies_index'),
    path('create-new', views.create_new, name='movies_create'),
    path('view/<int:movie_id>', views.view, name='movies_view'),
    path('edit/<int:movie_id>', views.edit, name='movies_edit'),
    path('delete/<int:movie_id>', views.delete, name='movies_delete'),
]
