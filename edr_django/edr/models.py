from django.db import models


class Image(models.Model):
    imgfile = models.FileField(upload_to='images/%Y/%m/%d')