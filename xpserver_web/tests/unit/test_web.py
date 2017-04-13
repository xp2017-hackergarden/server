from django.core.urlresolvers import resolve
from xpserver_web.views import main


def test_root_resolves_to_hello_world():
    found = resolve('/')
    assert found.func == main

