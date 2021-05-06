from django.db import models
from django.utils import timezone
from django.contrib import admin
from proj.settings import SHORTENED_HOST_NAME


# Create your models here.
class UserUrlStatus(models.Model):
    descr = models.CharField(max_length=30)

    def __str__(self):
        return self.descr

    class Meta:
        db_table = "user_url_status"


class UserUrl(models.Model):
    user_url = models.CharField(max_length=2000)
    create_date = models.DateTimeField('date created', default=timezone.now)
    pub_date = models.DateTimeField('date published', null=True)
    resolve_path = models.CharField(max_length=12, default='')
    resolve_host = models.CharField(max_length=16, default=SHORTENED_HOST_NAME)
    user_domain = models.CharField(max_length=100)
    status = models.ForeignKey(UserUrlStatus, default=1, on_delete=models.RESTRICT)
    block_reason = models.CharField(max_length=120, null=True)
    block_date = models.DateTimeField('date blocked', null=True)

    class Meta:
        db_table = "user_url"
        indexes = [
            models.Index(fields=['resolve_host']),
            models.Index(fields=['resolve_path', 'resolve_host']),
            models.Index(fields=['user_domain', 'status']),
        ]

    @admin.display(
        boolean=False,
        ordering='-pub_date',
        description='short url',
    )
    def short_url_no_schema(self):
        return self._short_url(schema='')

    def short_url_http(self):
        return self._short_url(schema='http')

    def short_url_https(self):
        return self._short_url(schema='https')

    def _short_url(self, schema='https'):
        if len(self.resolve_host == 0 or len(self.resolve_path == 0)):
            return ''
        if len(schema) == 0:
            return str(self.resolve_host) + '/' + str(self.resolve_path)
        return str(schema) + '://' + str(self.resolve_host) + '/' + str(self.resolve_path)

class BlockedDomain(models.Model):
    domain = models.CharField(max_length=100)
    block_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "blocked_domain"

