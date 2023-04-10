from django.db import models


# Create your models here.
class Magazine(models.Model):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    QUARTERLY = 'quarterly'
    BIANNUAL = 'biannual'
    ANNUAL = 'annual'

    FREQUENCY_CHOICES = [(DAILY, 'Daily'),
                         (WEEKLY, 'Weekly'),
                         (MONTHLY, 'Monthly'),
                         (QUARTERLY, 'Quarterly'),
                         (BIANNUAL, 'Biannual'),
                         (ANNUAL, 'Annual'),
                         ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)

    def __str__(self):
        return self.name
