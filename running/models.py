from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from datetime import datetime, timedelta, timezone, tzinfo
from datetime import date 


class User(AbstractUser):
    pass

class Run(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=1000, blank=True)
    track = models.CharField(max_length=200, blank=True)
    distance = models.DecimalField(decimal_places=2, max_digits=5)
    time = models.CharField(max_length=64)
    pace = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    date = models.DateField(default=datetime.now)


    def serialize(self,user):
        return {
            "number": self.meal_notes,
            "title": self.title,
            "track": self.track,
            "distance": self.distance,
            "time":self.time,
            "pace": self.pace,
            "date":self.date
        } 

class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week = models.IntegerField()
    day = models.IntegerField()
    completed = models.BooleanField(default=False)

    def serialize(self,user):
        return {
            "week": self.week,
            "day": self.day,
            "completed": self.completed
        }
