from proj.settings import SHORTENED_HOST_NAME
from .models import UserUrl, UserUrlStatus
from django.utils import timezone
from random import randrange


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


class MakeShortPathService:

    def makeShortPath(self, user_url: UserUrl) -> bool:
        """
        I think we use 62 symbols [a-zA-Z0-9]
        And simply fill randomly our 7 symbols until our crontask (which we create later) shows us,
        that we filled up to 3% of 62 ** 7
        Then we start using 8 symbols. And so on.
        10 dice rolling attempts with only 3% filled kinda guarantee us 99.99999% of success,
        which close to any reasonable hosting uptime. So we good people always...
        """
        if 'gen_short_path_attempts' not in user_url.__dict__:
            user_url.gen_short_path_attempts = 0
        user_url.gen_short_path_attempts +=1
        if user_url.gen_short_path_attempts > 7:
            return False
        hash = self.makeRndHash()
        qs = UserUrl.objects.filter(resolve_path=hash)
        if qs.count() > 0:
            return self.makeShortPath(user_url=user_url)
        try:
            user_url.status_id = 2
            user_url.resolve_path = hash
            if not user_url.resolve_host:
                user_url.resolve_host = SHORTENED_HOST_NAME
        except Exception:
            return self.makeShortPath(user_url=user_url)

        return True


    def makeRndHash(self, length=7):
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        ls = len(s)
        res = ''
        for i in range(length):
            r = randrange(ls)
            res += s[r]
        return res