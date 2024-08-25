from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    college = models.CharField(max_length=100)
    passing_year = models.PositiveIntegerField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

