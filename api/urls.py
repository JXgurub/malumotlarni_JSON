from django.urls import path
from .views import BotUserApiView


urlpatterns = [
    path("",BotUserApiView.as_view(),name="bot-user"),
]
