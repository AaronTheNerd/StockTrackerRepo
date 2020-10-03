from django.db import models
from django.urls import reverse

# Create your models here.
class Stock(models.Model):
    """The model represents an individual ticker."""
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=5)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """String for representing the stock."""
        return self.symbol

    def get_absolute_url(self):
        """Returns the url to access a detail record for this stock."""
        return reverse('in-depth', args=[self.symbol])
