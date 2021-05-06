from django.urls import path
from . import views


app_name = 'urlshortener'
urlpatterns = [
    # ex: /fafweOj6/
    path('<str:resolve_path>/', views.redirectView, name='redirectView'),
]
