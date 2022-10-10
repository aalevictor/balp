import uuid
from email.policy import default

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
        
    def create_user(self, twitch, email, password=None):
        if not twitch:
            raise ValueError('Username é obrigatório.')

        user = self.model(
            twitch=twitch,
            email=email
        )
        user.set_password(password)
        user.save()

        return user

    def create_staffuser(self, twitch, email, password):
        user = self.create_user(
            twitch,
            email=email,
            password=password
        )
        user.is_staff = True
        user.save()

        return user

    def create_superuser(self, twitch, email, password):
        user = self.create_user(
            twitch,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name            = models.CharField(max_length=100)
    twitch          = models.CharField(max_length=100, unique=True)
    discord         = models.CharField(max_length=100, null=True, blank=True)
    email           = models.CharField(max_length=100, null=True, blank=True, default=None, unique=True)
    date_joined     = models.DateTimeField(auto_now_add=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
        
    objects = UserManager()

    USERNAME_FIELD = 'twitch'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return '{}({})'.format(self.name, self.twitch)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
