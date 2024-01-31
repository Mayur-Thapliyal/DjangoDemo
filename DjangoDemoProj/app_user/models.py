from django.db import models
from app_user.util import *
class UsersBaseModel(models.Model):
    name                =       models.CharField(null = False)
    created_at          =       models.DateTimeField(auto_now_add=True)
    updated_at          =       models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'users'
        abstract = True
# Create your models here.
class UserModel(UsersBaseModel):
    password=models.CharField(null=False,max_length = 255,validators=[validate_password])
    phone_no=models.CharField(null=False,max_length = 50,validators=[validate_phone_number])
    email = models.CharField(null=False,max_length = 255,validators=[validate_email])
    gender = models.CharField(null=True,max_length = 50)
    class Meta:
        db_table = "app_user_model"