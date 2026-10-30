from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('ADMIN', 'Admin'),
    ('CASHIER', 'Cashier'),
    ('MANAGER', 'Manager'),
)


# Create your models here.
class POSUser(AbstractUser):
    first_name = models.CharField(
        max_length=20,
        null=False,
    )
    last_name = models.CharField(
        max_length=50,
        null=False
    )
    role = models.CharField(
        choices=ROLE_CHOICES
    )

    USERNAME_FIELD = 'username'