from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from .util import *
from django.utils import timezone



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    category=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.category


class Post(models.Model):
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    heading=models.TextField(max_length=500)
    body=RichTextUploadingField(blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null= True)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    creation_date=models.DateTimeField(default=timezone.now)
    thumb_url=models.CharField(max_length=200,default="{% static 'images/blogimage.jpg' %}")


@receiver(pre_save, sender=Post)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
	    instance.slug = unique_slug_generator(instance)




	# id->primary key
	# user ->foriegn key user
	# category ->many to many field category
	# heading
	# body
	# date created->creation date
	# likes
	# dislikes

