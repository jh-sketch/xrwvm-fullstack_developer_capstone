from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
    ]

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV'
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ],
        default=2023
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
