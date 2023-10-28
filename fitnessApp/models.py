# Create your models here.
from django.db import models
from django.contrib.auth.models import User

GOAL_BODY_TYPE = (
    ("LEAN", "Lean"),
    ("BUFF", "Buff"),
    ("CUT", "Cut"),
    ("BULK", "Bulk")
)

#Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bmi = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    goalBodyType = models.CharField(
        maxLength = 20,
        choices = GOAL_BODY_TYPE,
        default = 'LEAN'
    )
    def str(self):
        return self.user.username
    
