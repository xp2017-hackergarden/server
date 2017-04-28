from django.core.urlresolvers import resolve
from xpserver_web.views import main, register, change_password


def test_root_resolves_to_main():
    found = resolve('/')
    assert found.func == main


def test_register_resolves_to_register():
    found = resolve('/register/')
    assert found.func == register


def test_change_password_resolves_to_change_password():
    found = resolve('/change-password/')
    assert found.func == change_password
