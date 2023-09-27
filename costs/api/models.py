from django.db import models

class Cost(models.Model):
  CHOICES = (
    ("Supermarkets", "Supermarkets"),
    ("Accounts", "Accounts"),
    ("Other", "Other")
  )

  description = models.TextField()
  amount = models.FloatField()
  date = models.TextField()
  category = models.CharField(max_length=15, choices=CHOICES)
