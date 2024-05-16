from django.db import models
from main.models import Account
# Create your models here.
import random
from django import forms
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

class ReservationForm (forms.ModelForm): 
    TIMES = [
        ['09:00-12:00', '09:00-12:00'],
        ["13:00-16:00", '13:00-16:00'],
        ['17:00-20:00', '17:00-20:00']
    ]
    class Meta: 
        model = Reservations
        fields = ['Name', 'Date', 'Time', 'people', 'space', 'id']
        widgets = {
            'Name': forms.HiddenInput(),
            'Date': forms.DateInput(attrs={'type': 'date'}),
            'Time': forms.Select(),
            'people': forms.NumberInput(attrs={'min': 1, 'max': 14}),
            'space': forms.Select(), 
            'id': forms.HiddenInput()
        }
    
    Time = forms.ChoiceField(choices=TIMES)

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        super(ReservationForm, self).__init__(*args, **kwargs)
        # self.fields['Name'].queryset = Account.objects.filter(username=kwargs['initial']['Name'])
        # self.fields['Name'].initial = kwargs['initial']['Name']
        name = initial.get('Name', None)
        id = initial.get('id', None)
        if name:
            self.fields['Name'].queryset = Account.objects.filter(username=name)
            self.fields['Name'].initial = name
        if id:
            self.fields['id'].initial = id
        
        self.fields['space'].initial = 'A'
        self.fields['space'].choices = self.Meta.model.SPACE
        self.fields['space'].label = 'Space'
        self.fields['Name'].label = 'Name'
        self.fields['Date'].label = 'Date'
        self.fields['Time'].label = 'Time'
        self.fields['people'].label = 'People'