# file sanic/headers.py:63-98
# lines [63, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 81, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 95, 96, 98]
# branches ['70->71', '70->72', '73->74', '73->76', '79->81', '79->98', '81->83', '81->87', '83->84', '83->86', '92->93', '92->95', '95->79', '95->96']

import pytest
from sanic.headers import parse_forwarded
from unittest.mock import Mock

def test_parse_forwarded_with_secret():
    headers = Mock()
    headers.getall.return_value = ['by=secret;for=192.0.2.60;proto=http;host=example.com']
    config = Mock()
    config.FORWARDED_SECRET = 'secret'

    result = parse_forwarded(headers, config)

    assert result is not None
    assert 'by' in result
    assert result['by'] == 'secret'

def test_parse_forwarded_without_secret():
    headers = Mock()
    headers.getall.return_value = ['by=notsecret;for=192.0.2.60;proto=http;host=example.com']
    config = Mock()
    config.FORWARDED_SECRET = 'secret'

    result = parse_forwarded(headers, config)

    assert result is None

def test_parse_forwarded_no_headers():
    headers = Mock()
    headers.getall.return_value = None
    config = Mock()
    config.FORWARDED_SECRET = 'secret'

    result = parse_forwarded(headers, config)

    assert result is None

def test_parse_forwarded_no_secret_in_config():
    headers = Mock()
    headers.getall.return_value = ['by=secret;for=192.0.2.60;proto=http;host=example.com']
    config = Mock()
    config.FORWARDED_SECRET = None

    result = parse_forwarded(headers, config)

    assert result is None
