from django.db import models


# Create your models here.
class Articles(models.Model):
    name = models.CharField(max_length=50)
    mini_description = models.CharField(max_length=217)
    main_article = models.TextField()
    img = models.ImageField(upload_to='images/')