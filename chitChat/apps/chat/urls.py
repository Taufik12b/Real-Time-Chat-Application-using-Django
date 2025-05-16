from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.chatRoom, name="chat"),
    path('<str:username>/get_messages/', views.get_messages, name="get_messages"),
]
