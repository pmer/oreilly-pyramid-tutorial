from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2'
]
setup(name='mysite',
      install_requires=requires,
      # place of plug in points for other packages in this package
      # currently being used to defines location to be used to get a WSGI application (web services gateway interface)
      # in our case it is the the main function in the mysite package
      entry_points="""\
      [paste.app_factory]
      main = mysite:main
      """
      )
