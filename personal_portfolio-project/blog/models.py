from django.db import models

# Create your models here.
class ProjectBlogFlo(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True) 
    date = models.DateField()
