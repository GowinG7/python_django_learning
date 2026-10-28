from django.db import models
from django.utils import timezone

# Create your models here.
class GGmomo(models.model):
    GGmomo_TYPE_CHOICE = [
        ('Ch','Chicken'),
        ('Mu','Mutton'),
        ("bu","Buff"),
        ('Ve','Veg'),
        ('Pa','Paneer'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ggmomo/')
    date_added = models.DateTimeField(default=timezone.now) 
    #TO make only available ggmomo type choice 
    type = models.CharField(max_length=2, choices=GGmomo_TYPE_CHOICE)