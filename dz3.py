
class Url:

    def __init__(self, scheme=None, authority=None, path=None, query=None, fragment=None):

        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        return str(self) == other

    def __str__(self):
        return f'{self.scheme}://{self.authority}{self.path}?{self.query}#{self.fragment}'


class HttpsUrl(Url):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.scheme = 'https'


class HttpUrl(Url):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.scheme = 'http'

class GoogleUrl(HttpsUrl):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.authority = 'google.com'


class WikiUrl(HttpsUrl):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.authority = 'wikipedia.org'


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
# assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
# assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'))
# assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'))

g = GoogleUrl()
print(g)




