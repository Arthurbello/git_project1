from django.contrib.auth.models import User
from django.db import models

# class PhoneUser(AbstractUser):
#     phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u"{}".format(self.name)


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='posts')
    category = models.ForeignKey(Categories, related_name='category')

    def __unicode__(self):
        return u"{}".format(self.title)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name='post')

    def __unicode__(self):
        return u"{}".format(self.name)

# class Profile(models.Model):
#    user = models.OneToOneField(User)
#    first_name = models.CharField(max_length = 20)
#    last_name = models.CharField(max_length = 20)
#    bio = models.TextField()
#    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
#    last_modified = models.DateTimeField(auto_now_add=True)
