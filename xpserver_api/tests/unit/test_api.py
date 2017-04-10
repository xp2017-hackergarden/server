import pytest

from xpserver_api.views import hello_world

def test_hello_world(client):
    response = client.get('/api/hello_world')
    assert response.content.decode('utf-8') == 'hello world'
