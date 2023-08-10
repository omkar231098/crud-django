# crud_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:person_id>/', views.update, name='update'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
]
