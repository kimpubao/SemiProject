from django.db import models

# Create your models here.
class News(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    link = models.TextField()
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject