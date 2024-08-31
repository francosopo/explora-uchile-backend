from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        username = self.normalize_username(username)
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
