
class Url:

    def __init__(self, scheme=None, authority=None, path=None, query=None, fragment=None):

        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        url = ''
        if self.scheme:
            url += f'{self.scheme}:'
        if self.authority:
            url += f'//{self.authority}'
        if self.path:
            for p in self.path:
                url += f'/{p}'
        if self.query:
            url += '?' + '&'.join(f'{k}={v}' for k, v in self.query.items())
        if self.fragment:
            url += '#' + '&'.join(f'{k}={v}' for k, v in self.fragment.items())

        return url


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
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'


# Реализовать класс UrlCreator, с помощью которого можно будет создавать Url:
# При вызове метода _create должен возвращать Url
# Конструктор должен принимать параметры scheme и authority
# Методы __getattr__ и __call__ должны быть переопределены
# *args от __call__ должны добавлять этапы в лист path
# __getattr__ должен добавлять один этап в лист path


class UrlCreator:

    def __init__(self, scheme, authority, path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def _create(self):
        return Url(scheme=self.scheme, authority=self.authority, path=self.path, query=self.query,
                   fragment=self.fragment)


    def __str__(self):
        url = ''
        if self.scheme:
            url += f'{self.scheme}:'
        if self.authority:
            url += f'//{self.authority}'
        if self.path:
            for p in self.path:
                url += f'/{p}'
        if self.query:
            url += '?' + '&'.join(f'{k}={v}' for k, v in self.query.items())
        if self.fragment:
            url += '#' + '&'.join(f'{k}={v}' for k, v in self.fragment.items())

        return url

    def __eq__(self, other):
        return str(self) == str(other)


    def __call__(self, *args, **kwargs):

        if self.path:
            p = self.path + [arg for arg in args]
        else:
            p = [arg for arg in args]

        if self.query:
            q = self.query.update({k: v for k, v in kwargs.items()})
        else:
            q = {k: v for k, v in kwargs.items()}

        return UrlCreator(self.scheme, self.authority, path=p, query=q)

    def __getattr__(self, name):
        if self.path:
            p = self.path + [name]
        else:
            p = [name]
        return UrlCreator(self.scheme, self.authority, path=p)



url_creator = UrlCreator(scheme='https', authority='docs.python.org')
assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
assert url_creator('api','v1','list') == 'https://docs.python.org/api/v1/list'
assert url_creator('api','v1','list', q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'
assert url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create()  ==\
       'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'











