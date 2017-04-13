from django.core.urlresolvers import resolve
from xpserver_web.views import main, register


def test_root_resolves_to_main():
    found = resolve('/')
    assert found.func == main


def test_register_resolves_to_main():
    found = resolve('/register/')
    assert found.func == register
