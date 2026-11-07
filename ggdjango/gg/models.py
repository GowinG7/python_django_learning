from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# Yeha GGmomo class bnya momo ko types haru ko lagi class
class GGmomo(models.Model):
    GGmomo_TYPE_CHOICE = [
        ("Ch", "Chicken"),
        ("Mu", "Mutton"),
        ("bu", "Buff"),
        ("Ve", "Veg"),
        ("Pa", "Paneer"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="ggmomo/")
    date_added = models.DateTimeField(default=timezone.now)
    # TO make only available ggmomo type choice
    type = models.CharField(max_length=2, choices=GGmomo_TYPE_CHOICE)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    # django ko admin ko default behavior chaie pularize grne raixa
    # from GGmomo to G gmomo and also spilts it into two words as there are two capital words starting so its django default behavior

    class Meta:
        verbose_name = "GG Momo"
        verbose_name_plural = "GG Momos"


# One to Many
class momoReview(models.Model):
    # related name chaie tyo table maa k naam le identify hune or table ko reference for this
    momo = models.ForeignKey(GGmomo, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateField(default=timezone.now)


def __str__(self):
    return f"{self.user.username} review for {self.momo.name}"


# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    momo_varieties = models.ManyToManyField(GGmomo, related_name="stores")

    def __str__(self):
        return self.name


# One to One
class momoCertificate(models.Model):
    momo = models.OneToOneField(
        GGmomo, on_delete=models.CASCADE, related_name="certificate"
    )
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()


def __str__(self):
    return f"Certificate for {self.name.momo}"
