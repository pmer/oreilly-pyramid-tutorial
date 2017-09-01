from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, notfound_view_config

sample_todos = {
    '1': dict(id='1', title='get milk'),
    '2': dict(id='2', title='get eggs')
}

# - check out @view_defaults to define a series of view functions that share a route
# - but differ in another way for example by their request_method ie. GET, POST, DELETE, PUT
# - classes are ideal for sharing state, computation, or other kinds of coupling
# - when transitioning from view functions to a function class all the parameter we passed called request should change to self


class MySite:
    def __init__(self, request):
        self.request = request

    # using @property we don't have to call it with parenthesis in the template
    @property
    def current(self):
        todo_id = self.request.matchdict.get('id')
        todo = sample_todos.get(todo_id)
        if not todo:
            raise HTTPNotFound()
        return todo

    @notfound_view_config(renderer='templates/notfound.jinja2')
    def not_found(self):
        return dict()

    @view_config(route_name='list',
                 renderer='templates/list.jinja2')
    def list(self):
        # if message was found extract and provide it to the template
        msg = self.request.params.get('msg')
        return dict(
            todos=sample_todos.values(),
            msg=msg
        )

    @view_config(route_name='add',
                 renderer='templates/add.jinja2')
    def add(self):
        return dict()

    @view_config(route_name='view',
                 renderer='templates/view.jinja2')
    def view(self):
        return dict(todo=self.current)

    @view_config(route_name='edit',
                 renderer='templates/edit.jinja2')
    def edit(self):
        return dict(todo=self.current)

    # the parameters passed to @view_config are all examples of predicates
    # what is an example of a custom predicate?
    @view_config(route_name='edit',
                 renderer='templates/edit.jinja2',
                 request_method='POST',
                 request_param='form.submit')
    def edit_handler(self):
        new_title = self.request.params.get('new_title')
        # print('New title', new_title)
        self.current['title'] = new_title
        msg = 'new_title: ' + new_title
        url = self.request.route_url('list', _query={'msg':msg})
        return HTTPFound(url)

    @view_config(route_name='delete')
    def delete(self):
        url = self.route_url('list')
        return HTTPFound(url)
