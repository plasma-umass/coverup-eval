# file: lib/ansible/module_utils/urls.py:1522-1541
# asked: {"lines": [1522, 1523, 1524, 1525, 1526, 1527, 1528, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541], "branches": []}
# gained: {"lines": [1522, 1523, 1524, 1525, 1526, 1527, 1528, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541], "branches": []}

import pytest
from ansible.module_utils.urls import open_url
from unittest.mock import patch, MagicMock
import urllib.error
import urllib.request

def test_open_url_get(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "http://example.com"
    response = open_url(url)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_post(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "http://example.com"
    data = "data"
    response = open_url(url, data=data)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_with_headers(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "http://example.com"
    headers = {"Custom-Header": "value"}
    response = open_url(url, headers=headers)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_with_auth(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "http://example.com"
    url_username = "user"
    url_password = "pass"
    response = open_url(url, url_username=url_username, url_password=url_password)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_with_proxy(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "http://example.com"
    response = open_url(url, use_proxy=False)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_with_ssl(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "https://example.com"
    response = open_url(url, validate_certs=False)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_with_timeout(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "http://example.com"
    response = open_url(url, timeout=5)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_with_redirects(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "http://example.com"
    response = open_url(url, follow_redirects='all')

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_with_client_cert(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "https://example.com"
    client_cert = "/path/to/cert"
    client_key = "/path/to/key"
    response = open_url(url, client_cert=client_cert, client_key=client_key)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"

def test_open_url_with_cookies(monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b"response"
    mock_urlopen = MagicMock(return_value=mock_response)
    monkeypatch.setattr(urllib.request, 'urlopen', mock_urlopen)

    url = "http://example.com"
    cookies = MagicMock()
    response = open_url(url, cookies=cookies)

    mock_urlopen.assert_called_once()
    assert response.read() == b"response"
