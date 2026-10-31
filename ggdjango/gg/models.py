from django.db import models
from django.utils import timezone

# Create your models here.
class GGmomo(models.Model):
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
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        return self.name
# django ko admin ko default behavior chaie pularize grne raixa
# from GGmomo to G gmomo and also spilts it into two words as there are two capital words starting so its django default behavior

    class Meta:
        verbose_name = "GG Momo"
        verbose_name_plural = "GG Momos"