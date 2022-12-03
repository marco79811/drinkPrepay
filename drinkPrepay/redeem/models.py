from django.db import models
from django.contrib.auth import get_user_model

from cafe.models import Coffee


# Create your models here.

Customer = get_user_model()


class Redeem(models.Model):
    user = models.ForeignKey(
        to=Customer, 
        on_delete=models.PROTECT, 
        related_name='redeem',
    )

    coffee = models.ManyToManyField(to=Coffee, related_name='coffee')

