from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    imperial = 'imperial'
    metric = 'metric'
    units_choices = [(imperial, 'imperial'), (metric, 'metric')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(default='State College, USA', max_length = 200)
    units = models.CharField(choices=units_choices, default=metric, max_length = 100)

    def __str__(self):
        return f'{self.user.username} Profile'