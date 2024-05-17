from django.db import models

class News(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField(null=True)
    create_date = models.DateTimeField(null=True)
    news_date = models.DateTimeField(null=True)
    link = models.TextField(null=True)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject