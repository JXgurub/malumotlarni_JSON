from .models import BotUser
from rest_framework.serializers import ModelSerializer



class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('name','username','user_id', 'created_at')
        
        