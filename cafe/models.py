from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


class Cafe(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    main_image_url = models.URLField()

    def __str__(self):
        return self.name

class CafeImage(models.Model):
    cafe = models.ForeignKey(to=Cafe , related_name='all_images')
    image_url = models.URLField()

#
# class UserInfo(models.Model):
#     user = models.ForeignKey(User, related_name='additionals')
#     is_active = models.BooleanField(default=False)
    #
    # def __str__(self):
    #     return self.user.username
