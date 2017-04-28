from django.core.urlresolvers import resolve
from xpserver_api.views import activate_account, activate_mobile_app


def test_activate_account_resolves_to_activate_mobile_app():
    found = resolve('/api/activate-account/')
    assert found.func == activate_account


def test_activate_mobile_app_resolves_to_activate_mobile_app():
    found = resolve('/api/activate-mobile-app/')
    assert found.func == activate_mobile_app
