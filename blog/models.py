from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:200]

    def __str__(self):
        return self.title
