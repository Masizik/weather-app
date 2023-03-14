from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class HistoryModel(models.Model):
    country_code = models.TextField(
        blank=False,
        null=False,
    )
    country_name = models.TextField(
        blank=False,
        null=False,
    )
    city_name = models.TextField(
        blank=False,
        null=False,
    )
    latitude = models.FloatField(
        blank=False,
        null=False,
    )
    longitude = models.FloatField(
        blank=False,
        null=False,
    )
    timezone = models.TextField(
        blank=False,
        null=False,
    )
    population = models.TextField(
        blank=False,
        null=False,
    )
    create_date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


