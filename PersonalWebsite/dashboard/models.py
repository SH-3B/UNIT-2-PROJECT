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
    CATEGORY_CHOICES = [
        ('city', 'Favorite City'),
        ('drink', 'Favorite Drink'),
        ('quote', 'Favorite Quote'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=True)
    quote = models.TextField(null=False, blank=True)
    meaning = models.TextField(null=True, blank=True)
    why_chose = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='interest_images/', blank=True, null=True) 
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True,
        default='city',  
    )

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
