from django.contrib.auth.models import AbstractUser
from django.db import models

class PhoneUser(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")


class Comment(models.Model):
    username = models.ForeignKey(PhoneUser)
    content = models.TextField(max_length=140)



