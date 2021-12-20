from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=50, unique=True)

    def __srt__(self):
        return self.top_name

class web(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, null=True)    
    name = models.CharField(max_length=40)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(web, on_delete=models.DO_NOTHING, null=True)
    date = models.DateField()

    def __str__(self):
        return str(self.date)