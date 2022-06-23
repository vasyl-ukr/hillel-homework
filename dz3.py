
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

# g = GoogleUrl(query={'q': 'python', 'result': 'json'})
# w = WikiUrl(path=['wiki', 'python'])
# print(g, w)

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

    # def __getattr__(self, name):
    #     if self.path:
    #         self.path.append(name)
    #     else:
    #         self.path = [name]
    #     return UrlCreator(scheme=self.scheme, authority=self.authority, path=self.path)


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

        def varname(var):
            return [name for name in globals() if globals()[name] is var][0]

        arg_name = [varname(arg) for arg in args]

        if self.path:
            self.path += arg_name
        else:
            self.path = arg_name

        if self.query:
            self.query.update({k: v for k, v in kwargs.items()})
        else:
            self.query = {k: v for k, v in kwargs.items()}

        return self

    def __getattr__(self, name):
        if self.path:
            p = self.path + [name]
        else:
            p = [name]
        return UrlCreator(self.scheme, self.authority, path=p)



url_creator = UrlCreator(scheme='https', authority='docs.python.org')
assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
assert url_creator(api,v1,list) == 'https://docs.python.org/api/v1/list'











