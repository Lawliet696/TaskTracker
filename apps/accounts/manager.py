from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, login, password):
        if not login:
            raise ValueError('Login must be provided')

        user = self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, login, password, **kwargs):
        user = self.create_user(login, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
