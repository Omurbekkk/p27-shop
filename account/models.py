from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .utils import send_activation_code

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, phone, **kwargs):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)  # переводит все в нижний регистр (привели в порядок)
        user = self.model(email=email, phone=phone, **kwargs) # создали юзера без пароля
        # self.model == User
        user.set_password(password)   # хеширование пароля
        user.create_activation_code()   # генерируем актив/код
        send_activation_code(user.email, user.activation_code)   # Отправляем на почту
        user.save(using=self._db)   # сохраняем юзера в базу данных
        return user     # и сохраняем нашего юзера

    # это все было для обычного юзера
    # а теперь для суперюзера
    # суперюзер имеет доступ в админ ( отличие )
    def create_superuser(self, email, password, phone, **kwargs):
        if not email:
            raise ValueError('Email is required')

        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True

        # остальное все то же самое

        email = self.normalize_email(email)  # переводит все в нижний регистр (привели в порядок)
        user = self.model(email=email, phone=phone, **kwargs) # создали юзера без пароля
        # self.model == User
        user.set_password(password)   # хеширование пароля
        user.save(using=self._db)   # сохраняем юзера в базу данных
        return user     # и сохраняем нашего юзера




class User(AbstractUser):
    username = None  # убираем username из полей
    email = models.EmailField(unique=True)  # когда регитр-ся чтобы выходило "Польз-ль с таким имененем уже сущ-ет
    phone = models.CharField(max_length=50)
    bio = models.TextField()
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)


    USERNAME_FIELD = 'email'    # указываем какое поле использовать при логине
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()    # указываем нового менеджера

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(length=8)
        self.activation_code = code
        self.save()

