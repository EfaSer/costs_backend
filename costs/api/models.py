from django.db import models

class Cost(models.Model):

  description = models.TextField()
  amount = models.FloatField()
  date = models.TextField()
