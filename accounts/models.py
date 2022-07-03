from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self,name,cnic, password,guardian=None,contact=None):
        if not name:
            raise ValueError("Users must have a name")

        user = self.model(
            name = name,
            guardian = guardian,
            contact = contact,
            cnic = cnic,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,name,cnic, password,guardian=None,contact=None):
        if not name:
            raise ValueError("Users must have a name")
        user = self.create_user(
            name = name,
            password = password,
            guardian = guardian,
            contact = contact,
            cnic = cnic,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser):
    name                = models.CharField(max_length=60)
    guardian            = models.CharField(max_length=30, null=True)
    contact             = models.CharField(max_length=12, null=True)
    cnic                = models.TextField(primary_key=True, max_length=15, unique=True)
    status              = models.CharField(max_length=12, null=True, default="Active")

    date_joined         = models.DateTimeField(verbose_name = "date joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name = "last login", auto_now_add=True)
    is_active           = models.BooleanField(default=True)

    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    objects             = UserManager()

    USERNAME_FIELD      = "cnic"
    REQUIRED_FIELDS     = ["name",]

    def __str__(self):
        return self.cnic

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

