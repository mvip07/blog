from django.db import models
from django.urls import reverse

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField(max_length=1000)

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse('home', args=[str(self.pk)])
        