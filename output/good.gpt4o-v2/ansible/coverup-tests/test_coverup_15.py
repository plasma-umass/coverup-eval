# file: lib/ansible/module_utils/urls.py:673-745
# asked: {"lines": [673, 679, 680, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 694, 695, 697, 698, 699, 701, 702, 703, 704, 705, 707, 708, 712, 713, 714, 715, 716, 717, 719, 720, 721, 722, 723, 724, 725, 728, 729, 732, 733, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745], "branches": [[680, 683], [680, 712], [692, 694], [692, 695], [702, 703], [702, 707], [704, 705], [704, 708], [725, 728], [725, 729], [729, 732], [729, 735]]}
# gained: {"lines": [673, 679, 680, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 695, 697, 698, 708, 712, 713, 714, 715, 716, 717, 719, 720, 721, 722, 723, 724, 725, 728, 729, 732, 733, 735, 736, 737, 738, 739, 745], "branches": [[680, 683], [680, 712], [692, 695], [725, 728], [725, 729], [729, 732], [729, 735]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.urls import generic_urlparse, ParseResultDottedDict

def test_generic_urlparse_with_named_attributes():
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

    result = generic_urlparse(parts)

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

def test_generic_urlparse_with_ipv6():
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

    assert result['scheme'] == 'http'
    assert result['netloc'] == '[::1]:80'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query'
    assert result['fragment'] == 'fragment'
    assert result['username'] == None
    assert result['password'] == None
    assert result['hostname'] == '::1'
    assert result['port'] == 80

def test_generic_urlparse_with_indexed_attributes():
    parts = ('http', 'user:pass@hostname:80', '/path', '', 'query', 'fragment')

    result = generic_urlparse(parts)

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

def test_generic_urlparse_with_indexed_attributes_no_auth():
    parts = ('http', 'hostname:80', '/path', '', 'query', 'fragment')

    result = generic_urlparse(parts)

    assert result['scheme'] == 'http'
    assert result['netloc'] == 'hostname:80'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query'
    assert result['fragment'] == 'fragment'
    assert result['username'] == None
    assert result['password'] == None
    assert result['hostname'] == 'hostname'
    assert result['port'] == 80

def test_generic_urlparse_with_indexed_attributes_no_port():
    parts = ('http', 'user:pass@hostname', '/path', '', 'query', 'fragment')

    result = generic_urlparse(parts)

    assert result['scheme'] == 'http'
    assert result['netloc'] == 'user:pass@hostname'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query'
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'user'
    assert result['password'] == 'pass'
    assert result['hostname'] == 'hostname'
    assert result['port'] == None
