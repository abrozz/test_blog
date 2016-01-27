# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    message = models.TextField(verbose_name=u'Сообщение')
    dtc = models.DateTimeField(u'Дата создания')
    dtm = models.DateTimeField(null=True, blank=True, verbose_name=u'Дата модификации')
    def __unicode__(self):
        return self.message

    def published(self):
        return self.dtc >= timezone.now() - datetime.timedelta(days=1)
    def modification(self):
        return self.dtm >= timezone.now()
    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.pk})


