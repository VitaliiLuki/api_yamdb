from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Create and saves a user with unique email and username."""
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    USER_ROLES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )

    username = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Unique user name'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email of user'
    )
    role = models.CharField(
        max_length=20,
        choices=USER_ROLES,
        blank=True,
        default=USER,
        verbose_name='Role of user'
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='First name'
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Last name'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Biography'
    )
    confirmation_code = models.CharField(
        max_length=25,
        null=True
    )

    @property
    def is_user(self):
        return self.role == User.USER

    @property
    def is_moderator(self):
        return self.role == User.MODERATOR

    @property
    def is_admin(self):
        return (self.role == User.ADMIN or self.is_superuser
                or self.is_staff)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user'
            ),
        ]

    def __str__(self):
        return self.username
