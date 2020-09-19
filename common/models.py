from __future__ import unicode_literals

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from common.access.access import UserRole

from common.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    phone = models.CharField('phone', max_length=20, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'auth_user'

    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between. """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """ Returns the short name for the user. """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Sends an email to this User. """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @staticmethod
    def user_roles(user_id):
        try:
            user_role_list = UserRole.objects.filter(user_id=user_id)
            return set(user_role.role.code_role for user_role in user_role_list)
        except Exception as e:
            return set()

    @staticmethod
    def has_email(email):
        """ Does the user have such an email """
        return User.objects.filter(email=email).exists()
