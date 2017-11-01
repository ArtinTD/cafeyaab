from django.db import models


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