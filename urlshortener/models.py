from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib import admin
from proj.settings import SHORTENED_HOST_NAME
import hashlib
from urlshortener.exceptions import UserUrlExistsAlreadyException


class UserUrlStatus(models.Model):
    descr = models.CharField(max_length=30)

    def __str__(self):
        return self.descr

    class Meta:
        db_table = "user_url_status"


class UserUrl(models.Model):
    user_url = models.CharField(max_length=2000)
    user_url_hash = models.CharField(max_length=32, default='' )
    create_date = models.DateTimeField('date created', default=timezone.now)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    resolve_path = models.CharField(max_length=12, default='')
    resolve_host = models.CharField(max_length=16, default=SHORTENED_HOST_NAME)
    user_domain = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(UserUrlStatus, default=1, on_delete=models.RESTRICT)
    block_reason = models.CharField(max_length=120, null=True, blank=True)
    block_date = models.DateTimeField('date blocked', null=True, blank=True)

    class Meta:
        db_table = "user_url"
        indexes = [
            models.Index(fields=['resolve_host']),
            models.Index(fields=['resolve_path', 'resolve_host']),
            models.Index(fields=['user_domain', 'status']),
            models.Index(fields=['user_url_hash']),
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
        if ((not self.resolve_host) or (not self.resolve_path)):
            return ''
        if not schema:
            return str(self.resolve_host) + '/' + str(self.resolve_path)
        return str(schema) + '://' + str(self.resolve_host) + '/' + str(self.resolve_path)

    def save(self, *args, **kwargs):
        h = self.makeUserUrlHash()
        if h != self.user_url_hash:
            self.user_url_hash = h
        if self.checkIfUserUrlExistsAlready(self):
            # raise UserUrlExistsAlreadyException("Url already in storage")
            pass #raise ValidationError({'user_url': ["error message", ]})
        super(UserUrl, self).save(*args, **kwargs)

    def makeUserUrlHash(self):
         return hashlib.md5(str(self.user_url).encode('utf-8')).hexdigest()

    def checkIfUserUrlExistsAlready(self, obj):
        found = UserUrl.objects.filter(user_url_hash=obj.user_url_hash).exclude(pk=obj.pk)
        return found.count() > 0


class BlockedDomain(models.Model):
    domain = models.CharField(max_length=100, unique=True)
    block_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "blocked_domain"
        indexes = [
            models.Index(fields=['domain']),
        ]

