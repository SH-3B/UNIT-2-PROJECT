from django.db import models
# Create your models here.

class Education(models.Model):
    uni_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    description = models.TextField()
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.uni_name

class Interest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='interest_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
