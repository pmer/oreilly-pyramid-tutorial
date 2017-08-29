# from pyramid.response import Response  -- simple way to pass text back to client requested view

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
# brings in the decorator
from pyramid.view import view_config


# this lets the view statement (top) be very close to the view function
@view_config(route_name='home_page', renderer='home.jinja2')
def hello(request):
    # return a dictionary of data instead of the raw html element; which was once passed with Response
    return dict(site_name='World')


@view_config(route_name='hello', renderer='hello.jinja2')
def hello_world(request):
    return dict(var="four letter word")


@view_config(route_name='hello', renderer='hello_name.jinja2',
             request_param='name')
def hello_name(request):
    name = request.params.get('name')
    return dict(name=name)

if __name__ == '__main__':
    # this thing is pretty important
    config = Configurator()
    # config jinja2; enables behaviour like, anything that ends in .jinja should be interpreted with jinja2
    config.include('pyramid_jinja2')
    config.add_route('home_page', '/')
    config.add_route('hello', '/hello')
    # find and process and configuration decorators in this package
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print ('Serving http://0.0.0.0:6543')
    server.serve_forever()
