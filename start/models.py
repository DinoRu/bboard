from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Albums(models.Model):
    title = models.CharField(max_length=300, unique=True)
    reference = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Albums, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name