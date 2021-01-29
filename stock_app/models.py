from django.db import models
from django.urls import reverse
from datetime import date

class Ticker(models.Model):
  tick = models.CharField(max_length = 6)

  

  def get_absolute_url(self):
    return reverse("ticker-detail", kwargs={"pk": self.pk})

  def __str__(self):
    return self.tick

class Price(models.Model):
  cost = models.DecimalField(max_digits=6, decimal_places=2)
  ticker = models.ForeignKey('Ticker', on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.cost
