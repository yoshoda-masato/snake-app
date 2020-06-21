import datetime
from django.db import models
from django.utils import timezone

class Pet(models.Model):
    name = models.CharField('ペットの名前', max_length=20)
    date = models.DateTimeField('日付', auto_now=True)
    nextdate = models.DateTimeField('次回日付', default=timezone.now())

    def save(self, *args, **kwargs):
        self.nextdate = timezone.now() + datetime.timedelta(weeks=1)
        super().save(*args, **kwargs)




