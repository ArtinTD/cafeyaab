from django.db import models
from django.contrib.auth.models import User

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


class UserInfo(models.Model):
    user = models.ForeignKey(User, related_name='additionals')
    username= models.CharField(max_length=20)
    email = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.user.username + ': ' + self.phone_number
