from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

# check out @view_defaults to define a series of view functions that share a route
# but differ in another way for example by their request_method ie. GET, POST, DELETE, PUT

# classes are ideal for sharing state, computation, or other kinds of coupling
class MySite:
    def __init__(self, request):
        self.request = request

    # using @property we don't have to call it with parenthesis in the template
    @property
    def current(self):
        return self.request.matchdict.get('id')

    @view_config(route_name='list',
                 renderer='templates/list.jinja2')
    def list(request):
        return dict()

    @view_config(route_name='add',
                 renderer='templates/add.jinja2')
    def add(request):
        return dict()

    @view_config(route_name='view',
                 renderer='templates/view.jinja2')
    def view(request):
        return dict()

    @view_config(route_name='edit',
                 renderer='templates/edit.jinja2')
    def edit(request):
        return dict()

    @view_config(route_name='delete')
    def delete(request):
        url = request.route_url('list')
        return HTTPFound(url)
