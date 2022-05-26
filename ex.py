from framework.wsgi import Framework
from jinja2 import Environment, PackageLoader, select_autoescape

from urls import my_urls


app = Framework(my_urls)

env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)

template = env.get_template("base.html")
print(template.render())
