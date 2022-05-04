from django.db import models

# Create your models here.


class Unicorn(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["location"]
