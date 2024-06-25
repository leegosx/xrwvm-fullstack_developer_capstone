from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(
        max_length=255, unique=True, help_text="Name of the car make"
    )
    description = models.TextField(help_text="Description of the car make")
    founded = models.DateField(
        null=True, blank=True, help_text="Date the company was founded"
    )
    country = models.CharField(
        max_length=100, blank=True, help_text="Country of origin"
    )


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name="models"
    )
    name = models.CharField(max_length=255, help_text="Name of the car model")
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ("COUPE", "Coupe"),
        ("HATCHBACK", "Hatchback"),
    ]

    type = models.CharField(
        max_length=50, choices=CAR_TYPES, help_text="Type of the car model"
    )
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)],
        help_text="Model year of the car",
    )
    is_available = models.BooleanField(
        default=True, help_text="Availability of the car model"
    )

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.type}"
