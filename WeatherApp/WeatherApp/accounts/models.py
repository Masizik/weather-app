from django.contrib.auth import models as auth_models
from django.core import exceptions
from django.core.validators import MinLengthValidator
from django.db import models


def only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Please type only letters!')


def only_digits(value):
    if not value.isdigit():
        raise exceptions.ValidationError('Please type only digits!')


def is_adult(value):
    if value < 18:
        raise exceptions.ValidationError('You must be at least 18 year old!')


# Create your models here.
class AppUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LEN = 6
    FIRST_NAME_MAX_LEN = 18
    LAST_NAME_MIN_LEN = 6
    LAST_NAME_MAX_LEN = 18

    email = models.EmailField(
        blank=False,
        null=False,
    )
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LEN,
                                  validators=(MinLengthValidator(FIRST_NAME_MIN_LEN), only_letters),
                                  blank=False,
                                  null=False,
                                  ),
    last_name = models.CharField(max_length=LAST_NAME_MAX_LEN,
                                 validators=(MinLengthValidator(LAST_NAME_MIN_LEN), only_letters),
                                 blank=False,
                                 null=False,
                                 ),
    age = models.IntegerField(validators=(is_adult,),
                              blank=True,
                              null=True, )
    picture = models.ImageField(upload_to='accounts_photos/',
                                blank=True,
                                null=True, )
