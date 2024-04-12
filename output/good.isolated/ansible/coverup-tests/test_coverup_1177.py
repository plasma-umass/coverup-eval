# file lib/ansible/module_utils/urls.py:673-745
# lines [694, 699, 701, 702, 703, 704, 705, 707, 735, 740, 741, 742, 743, 744]
# branches ['692->694', '702->703', '702->707', '704->705', '704->708', '725->729', '729->735']

import pytest
from ansible.module_utils.urls import generic_urlparse
from collections import namedtuple

# Define a namedtuple with the same attributes as a urlparse result
ParseResult = namedtuple('ParseResult', 'scheme netloc path params query fragment username password hostname port')

@pytest.fixture
def mock_parse_result_ipv6():
    # Create a mock ParseResult object with IPv6 address
    return ParseResult(
        scheme='http',
        netloc='[::1]:8080',
        path='/index.html',
        params='',
        query='user=test',
        fragment='section1',
        username='user',
        password='pass',
        hostname='::1',
        port=8080
    )

@pytest.fixture
def mock_parse_result_no_netloc():
    # Create a mock ParseResult object without netloc attribute
    return ('http', '', '/index.html', '', 'user=test', 'section1')

@pytest.fixture
def mock_parse_result_invalid_port():
    # Create a mock ParseResult object with invalid port
    return ParseResult(
        scheme='http',
        netloc='user:pass@[::1]:notaport',
        path='/index.html',
        params='',
        query='user=test',
        fragment='section1',
        username='user',
        password='pass',
        hostname='::1',
        port=None
    )

@pytest.fixture
def mock_parse_result_no_auth():
    # Create a mock ParseResult object without auth
    return ('http', 'example.com:8080', '/index.html', '', 'user=test', 'section1')

def test_generic_urlparse_ipv6(mock_parse_result_ipv6):
    result = generic_urlparse(mock_parse_result_ipv6)
    assert result['hostname'] == '::1'
    assert result['port'] == 8080

def test_generic_urlparse_no_netloc(mock_parse_result_no_netloc):
    result = generic_urlparse(mock_parse_result_no_netloc)
    assert result['hostname'] == ''
    assert result['port'] is None
    assert result['username'] is None
    assert result['password'] is None

def test_generic_urlparse_invalid_port(mock_parse_result_invalid_port):
    result = generic_urlparse(mock_parse_result_invalid_port)
    assert result['hostname'] == '::1'
    assert result['port'] is None

def test_generic_urlparse_no_auth(mock_parse_result_no_auth):
    result = generic_urlparse(mock_parse_result_no_auth)
    assert result['hostname'] == 'example.com'
    assert result['port'] == 8080
    assert result['username'] is None
    assert result['password'] is None
