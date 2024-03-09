from django.db import models


class BotUser(models.Model):
    user_id = models.CharField(max_length = 120)
    name = models.CharField(max_length= 120)
    username = models.CharField(max_length = 120)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
# Create your models here.
