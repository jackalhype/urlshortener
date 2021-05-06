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


class makeShortPathService:

    def makeShortPath(self) -> bool:
        """
        I think we use 62 symbols [a-zA-Z0-9]
        And simply fill randomly our 8 symbols untill our crontask (which we create later) shows us,
        that we filled up to 3% of 62 ** 8
        Then we start using 9 symbols. And so on.
        10 dice rolling attempts with only 3% filled kinda guarantee us 99.99999% of success,
        which close to any reasonable hosting uptime. So we good people always...
        """

