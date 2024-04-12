# file sanic/headers.py:63-98
# lines [68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 81, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 95, 96, 98]
# branches ['70->71', '70->72', '73->74', '73->76', '79->81', '79->98', '81->83', '81->87', '83->84', '83->86', '92->93', '92->95', '95->79', '95->96']

import pytest
from unittest.mock import MagicMock
from sanic.headers import parse_forwarded

@pytest.fixture
def mock_config():
    class MockConfig:
        FORWARDED_SECRET = "test_secret"
    return MockConfig()

def test_parse_forwarded_full_coverage(mock_config):
    headers = MagicMock()
    headers.getall.return_value = [
        'by=123;secret="test_secret";proto=http',
        'for=192.0.2.60;proto=http;by=203.0.113.43',
        'for=192.0.2.43, for=198.51.100.17'
    ]

    result = parse_forwarded(headers, mock_config)
    assert result is not None
    assert result == {'by': '123', 'secret': 'test_secret', 'proto': 'http'}

    headers.getall.return_value = None
    result = parse_forwarded(headers, mock_config)
    assert result is None

    headers.getall.return_value = [
        'by=123;secret="wrong_secret";proto=http'
    ]
    result = parse_forwarded(headers, mock_config)
    assert result is None

    headers.getall.return_value = [
        'by=123;secret="test_secret";proto=http',
        'for=192.0.2.60;proto=http;by=203.0.113.43'
    ]
    mock_config.FORWARDED_SECRET = None
    result = parse_forwarded(headers, mock_config)
    assert result is None
