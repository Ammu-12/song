from django.db import models

# Create your models here.
class Song(models.Model):
    sname=models.CharField(max_length=250)
    flyric=models.TextField()
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='picture')

    def __str__(self):
        return self.sname