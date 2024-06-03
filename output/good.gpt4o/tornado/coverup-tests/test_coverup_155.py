# file tornado/httpclient.py:59-88
# lines [59, 60]
# branches []

import pytest
from tornado.httpclient import HTTPClient, HTTPError
from unittest.mock import patch

def test_http_client_fetch_success(mocker):
    mock_response = mocker.Mock()
    mock_response.body = b"Success"
    
    with patch('tornado.httpclient.HTTPClient.fetch', return_value=mock_response):
        http_client = HTTPClient()
        response = http_client.fetch("http://www.example.com/")
        assert response.body == b"Success"
        http_client.close()

def test_http_client_fetch_http_error(mocker):
    mock_response = mocker.Mock()
    mock_response.code = 404
    mock_response.body = b"Not Found"
    
    with patch('tornado.httpclient.HTTPClient.fetch', side_effect=HTTPError(404, response=mock_response)):
        http_client = HTTPClient()
        with pytest.raises(HTTPError) as excinfo:
            http_client.fetch("http://www.example.com/")
        assert excinfo.value.code == 404
        assert excinfo.value.response.body == b"Not Found"
        http_client.close()

def test_http_client_fetch_other_error(mocker):
    with patch('tornado.httpclient.HTTPClient.fetch', side_effect=IOError("Network error")):
        http_client = HTTPClient()
        with pytest.raises(IOError) as excinfo:
            http_client.fetch("http://www.example.com/")
        assert str(excinfo.value) == "Network error"
        http_client.close()
