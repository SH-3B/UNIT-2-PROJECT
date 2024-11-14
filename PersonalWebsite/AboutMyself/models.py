from django.db import models
# Create your models here.

class Interest(models.Model):
    name = models.CharField(max_length=100, default="Default Interest")  # Add default here
    description = models.TextField()
    image = models.ImageField(upload_to='interests/', blank=True, null=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    uni_name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.uni_name
    
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
