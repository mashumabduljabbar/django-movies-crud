from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
	path('', lambda req: redirect('/movies/')),
    path('movies/', include('movies.urls')),
]
