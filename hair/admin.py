from django.contrib import admin
from django.contrib.auth.models import User
from hair.models import *

admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Comment)


