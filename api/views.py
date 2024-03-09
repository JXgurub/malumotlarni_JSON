from django.shortcuts import render
from .models import BotUser
from .serializers import BotUserSerializer
from rest_framework.generics import ListCreateAPIView


class BotUserApiView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
# Create your views here.
