class Request:

    # self.body = environ.get('wsgi.input')
    def __init__(self, environ: dict):
        self.method = environ['REQUEST_METHOD'].lower()
        self.query_params = self._get_query_params(environ)
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                headers[key[5:]] = value
        return headers

    def _get_query_params(self, environ):
        query_param = {}
        data = environ['QUERY_STRING'].split('&')
        for el in data:
            if el:
                key, value = el.split('=')
                if query_param.get(key):
                    query_param[key].append(value)
                else:
                    query_param[key] = [value]
        return query_param
