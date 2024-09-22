# accounts/backends.py
from django.contrib.auth.backends import BaseBackend
from accounts.models import Account

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
