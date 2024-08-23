
import json

from application.storage import storage


def test_store(test_app, monkeypatch):
    expected_url = "https://some-url.con/some/path"
    expected_token = "someToken"

    async def mockstore(url: str) -> str:
        assert expected_url == url
        return expected_token

    monkeypatch.setattr(storage, 'store', mockstore)
    
    payload = {"long_url": expected_url}
    response = test_app.post('/api/v1/short_urls/', content=json.dumps(payload))
    assert response.status_code == 201
    assert response.json() == {"token": expected_token}


def test_retrieve(test_app, monkeypatch):
    expected_url = "https://some-url.con/some/path"
    expected_token = "someToken"

    async def mockretrieve(token: str) -> str:
        assert token == expected_token
        return expected_url
    
    monkeypatch.setattr(storage, 'retrieve', mockretrieve)

    response = test_app.get(f'/api/v1/short_urls/{expected_token}')
    assert response.status_code == 200
    assert response.json() == {"url": expected_url}

