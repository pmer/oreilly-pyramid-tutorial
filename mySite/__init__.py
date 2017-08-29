from pyramid.config import Configurator

# new focus on the application not the serving of our application


# this code has been removed from __init__.py into views.py
# this makes the purpose this file more clear, the bootstrapping of the application
# which i think means configure
'''
from pyramid.view import view_config

@view_config(route_name='list', renderer='list.jinja2')
def list(request):
    return dict()
'''


# entry point tells us to come here, to main.
def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('list', '/')
    config.scan()
    return config.make_wsgi_app()

