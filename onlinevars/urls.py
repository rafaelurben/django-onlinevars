from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings

from . import views

#######################

app_name = 'onlinevars'
urlpatterns = [
    path('api/v1/<name>', views.api_v1, name="api-v1"),

    path('chat/', views.chat_start, name="chat-start"),
    path('chat/<postkey>/<mykey>/', views.chat, name="chat")
]
