from django.contrib import admin

# Register your models here.
from cafe.models import Cafe, UserInfo

admin.site.register([Cafe, UserInfo])