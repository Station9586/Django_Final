from django.db import models

# Create your models here.
class Account(models.Model): 
    username = models.CharField(max_length=200, primary_key=True, null=False)
    nickname = models.CharField(max_length=200, default='CAT')
    password = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.username

