from django.db import models


# Create your models here.
class Coffee(models.Model):
    class Status(models.IntegerChoices):
        DOWN = 0, '下架'  
        UP = 1, '上架'  

    name = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    status = models.SmallIntegerField(
        choices=Status.choices,
        default=Status.UP,
    
    )


    def __str__(self) -> str:
        return self.name



