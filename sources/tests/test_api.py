import json
import random

from application.lib.encoder import encode

def test_store(test_app, monkeypatch):
    def mockrandint(a: int, b: int) -> str:
        return 0
    
    monkeypatch.setattr(random, 'randint', mockrandint)
    
    payload = {'long_url': 'https://some-url.con/some/path'}
    response = test_app.post('/api/v1/short_urls/', content=json.dumps(payload))
    
    assert response.status_code == 201
    assert response.json() == {'token': encode(4000)}


def test_store_existing(test_app):
    payload = {'long_url': 'https://www.some-url.com/1'}
    response = test_app.post('/api/v1/short_urls/', content=json.dumps(payload))
    assert response.status_code == 201
    assert response.json() == {'token': 'TOc'}


def test_retrieve(test_app):
    response = test_app.get(f'/api/v1/short_urls/TOc')
    assert response.status_code == 200
    assert response.json() == {'url': 'https://www.some-url.com/1'}


def test_retieve_nonexisting(test_app):
    response = test_app.get(f'/api/v1/short_urls/random_token')
    assert response.status_code == 404
