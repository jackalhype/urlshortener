from urllib.parse import urlsplit

class UrlHelper:
    """
    urlsplit incorrect when no schema...
    """

    @classmethod
    def getDomain(cls, url):
        p = urlsplit(url)
        if not p.netloc:
            if not p.path:
                raise IncorrectUrlException('incorrect url %s' % url )
            p2 = urlsplit('https://' + p.path)
            if not p2.netloc:
                raise IncorrectUrlException('incorrect url %s' % url )
            return p2.netloc
        return p.netloc


class IncorrectUrlException(Exception):
    pass