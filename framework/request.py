class Request:
    def __init__(self, environ):
	    self.headers = self._get_http_headers(environ)
		self.method = None
		self.body = environ.get('wsgi.input')
		self.query_params = None
		self.path = environ.get('path')
		
	def _get_http_headers(self, environ):
	    headers = {}
		for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:]] = value
        return headers