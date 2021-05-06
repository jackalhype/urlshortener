from .models import UserUrl, UserUrlStatus
from django.utils import timezone


class BlockUserUrlsByDomainService:

    @classmethod
    def blockDomain(cls, domain: str):
        if not domain:
            return
        objs = UserUrl.objects.filter(user_domain=domain)
        status_blocked = UserUrlStatus.objects.get(pk=9)
        for obj in objs:
            obj.status = status_blocked
            obj.block_reason = 'domain blocked'
            obj.block_date = timezone.now()
            UserUrl.objects.bulk_update(objs, ['status', 'block_reason', 'block_date'])
