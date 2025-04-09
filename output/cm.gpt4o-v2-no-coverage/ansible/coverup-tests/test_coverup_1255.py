# file: lib/ansible/module_utils/urls.py:673-745
# asked: {"lines": [694, 699, 701, 702, 703, 704, 705, 707, 712, 713, 714, 715, 716, 717, 719, 720, 721, 722, 723, 724, 725, 728, 729, 732, 733, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744], "branches": [[680, 712], [692, 694], [702, 703], [702, 707], [704, 705], [704, 708], [725, 728], [725, 729], [729, 732], [729, 735]]}
# gained: {"lines": [712, 713, 714, 715, 716, 717, 719, 720, 721, 722, 723, 724, 725, 728, 729, 732, 733, 736, 737, 738, 739], "branches": [[680, 712], [725, 728], [729, 732]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.urls import generic_urlparse, ParseResultDottedDict

@pytest.fixture
def mock_parts_new():
    parts = Mock()
    parts.scheme = 'http'
    parts.netloc = 'user:pass@hostname:80'
    parts.path = '/path'
    parts.params = ''
    parts.query = 'query'
    parts.fragment = 'fragment'
    parts.username = 'user'
    parts.password = 'pass'
    parts.hostname = 'hostname'
    parts.port = 80
    return parts

@pytest.fixture
def mock_parts_old():
    return ('http', 'user:pass@hostname:80', '/path', '', 'query', 'fragment')

def test_generic_urlparse_new(monkeypatch, mock_parts_new):
    result = generic_urlparse(mock_parts_new)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'user:pass@hostname:80'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query'
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'user'
    assert result['password'] == 'pass'
    assert result['hostname'] == 'hostname'
    assert result['port'] == 80

def test_generic_urlparse_old(monkeypatch, mock_parts_old):
    result = generic_urlparse(mock_parts_old)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'user:pass@hostname:80'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query'
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'user'
    assert result['password'] == 'pass'
    assert result['hostname'] == 'hostname'
    assert result['port'] == 80

def test_generic_urlparse_ipv6(monkeypatch):
    parts = Mock()
    parts.scheme = 'http'
    parts.netloc = '[::1]:80'
    parts.path = '/path'
    parts.params = ''
    parts.query = 'query'
    parts.fragment = 'fragment'
    parts.username = None
    parts.password = None
    parts.hostname = '::1'
    parts.port = 80

    result = generic_urlparse(parts)
    assert result['hostname'] == '::1'
    assert result['port'] == 80

def test_generic_urlparse_invalid_port(monkeypatch):
    parts = Mock()
    parts.scheme = 'http'
    parts.netloc = 'hostname:invalid'
    parts.path = '/path'
    parts.params = ''
    parts.query = 'query'
    parts.fragment = 'fragment'
    parts.username = None
    parts.password = None
    parts.hostname = 'hostname'
    parts.port = None

    result = generic_urlparse(parts)
    assert result['hostname'] == 'hostname'
    assert result['port'] is None
