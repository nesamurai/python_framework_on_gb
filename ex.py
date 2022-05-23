from framework.wsgi import Framework
from urls import my_urls


app = Framework(my_urls)
