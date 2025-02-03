from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from PIL import Image


from .manager import CustomUserManager

class User(AbstractBaseUser):
    login = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email',]


    def __str__(self):
        return self.login


    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='username')
    tasks_completed = models.PositiveIntegerField(default=0)
    tasks_active = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    telegram = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.user.login

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

