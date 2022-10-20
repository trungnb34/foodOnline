from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        
        if not username:
            raise ValueError("User must have an user name")
        
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(
            username=username, 
            email=email, 
            password=password, 
            extra_fields=extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save()
        return user
        

class User(AbstractBaseUser):
    
    ROLE_CHOICE = (
        (1 , "Restaurant"),
        (2, "Customer")
    )
    
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    