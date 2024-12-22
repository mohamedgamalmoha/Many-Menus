from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True, null=True, verbose_name=_("Full Name"))
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Phone Number"))

    first_name = None
    last_name = None

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"