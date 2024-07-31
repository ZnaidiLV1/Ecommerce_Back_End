
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser, Group, \
    Permission
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    verification_code = models.CharField(max_length=6, default=100000, editable=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Set a unique related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Set a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.email


class EcommerceUser(models.Model):
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField()
    verification_code = models.UUIDField(default=100000, editable=True)
