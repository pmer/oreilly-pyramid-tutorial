from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config


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
    # the id we are looking for has been encoded in the route parameter
    # request.matchdict provides a dictionary for all of the matching route parameters
    # .get is used to avoid a python key error in case we ask for a parameter that is not in the dictionary
    current = request.matchdict.get('id')
    return dict(current=current)


@view_config(route_name='edit',
             renderer='templates/edit.jinja2')
def edit(request):
    current = request.matchdict.get('id')
    return dict(current=current)


@view_config(route_name='delete')
def delete(request):
    url = request.route_url('list')
    return HTTPFound(url)
