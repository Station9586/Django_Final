from django.db import models
from main.models import Account
# Create your models here.
import random

def random_id (): 
    ret = ""
    for i in range(0, 10):
        if (random.randint(0, 2) == 0): 
            ret += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            ret += str(random.choice('0123456789'))
    return ret

class Reservations (models.Model): 
    Name = models.ForeignKey(Account, on_delete=models.CASCADE)
    Date = models.CharField(max_length=20)
    Time = models.CharField(max_length=20)
    people = models.IntegerField(default=1)
    SPACE = [
        ['A', 'A'],
        ['B', 'B'],
        ['C', 'C'], 
        ['D', 'D']
    ]
    space = models.CharField(max_length=2, choices=SPACE, default='A')
    id = models.CharField(primary_key=True, default=random_id(), max_length=10)

    def __str__(self):
        return self.Name.username;

