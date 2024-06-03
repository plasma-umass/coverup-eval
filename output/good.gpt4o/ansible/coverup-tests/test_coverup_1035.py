# file lib/ansible/module_utils/urls.py:673-745
# lines [694, 699, 701, 702, 703, 704, 705, 707, 712, 713, 714, 715, 716, 717, 719, 720, 721, 722, 723, 724, 725, 728, 729, 732, 733, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744]
# branches ['680->712', '692->694', '702->703', '702->707', '704->705', '704->708', '725->728', '725->729', '729->732', '729->735']

import pytest
from ansible.module_utils.urls import generic_urlparse, ParseResultDottedDict
from urllib.parse import urlparse

def test_generic_urlparse_ipv6():
    url = 'http://[2001:db8::1]:8080/path?query=1#fragment'
    parts = urlparse(url)
    result = generic_urlparse(parts)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == '[2001:db8::1]:8080'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query=1'
    assert result['fragment'] == 'fragment'
    assert result['username'] is None
    assert result['password'] is None
    assert result['hostname'] == '2001:db8::1'
    assert result['port'] == 8080

def test_generic_urlparse_ipv6_no_port():
    url = 'http://[2001:db8::1]/path?query=1#fragment'
    parts = urlparse(url)
    result = generic_urlparse(parts)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == '[2001:db8::1]'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query=1'
    assert result['fragment'] == 'fragment'
    assert result['username'] is None
    assert result['password'] is None
    assert result['hostname'] == '2001:db8::1'
    assert result['port'] is None

def test_generic_urlparse_old_style():
    parts = ('http', 'user:pass@hostname:80', '/path', '', 'query=1', 'fragment')
    result = generic_urlparse(parts)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'user:pass@hostname:80'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query=1'
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'user'
    assert result['password'] == 'pass'
    assert result['hostname'] == 'hostname'
    assert result['port'] == 80

def test_generic_urlparse_old_style_no_auth():
    parts = ('http', 'hostname:80', '/path', '', 'query=1', 'fragment')
    result = generic_urlparse(parts)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'hostname:80'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query=1'
    assert result['fragment'] == 'fragment'
    assert result['username'] is None
    assert result['password'] is None
    assert result['hostname'] == 'hostname'
    assert result['port'] == 80

def test_generic_urlparse_old_style_no_port():
    parts = ('http', 'user:pass@hostname', '/path', '', 'query=1', 'fragment')
    result = generic_urlparse(parts)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'user:pass@hostname'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query=1'
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'user'
    assert result['password'] == 'pass'
    assert result['hostname'] == 'hostname'
    assert result['port'] is None

def test_generic_urlparse_old_style_invalid_netloc():
    parts = ('http', 'invalid_netloc', '/path', '', 'query=1', 'fragment')
    result = generic_urlparse(parts)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'invalid_netloc'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query=1'
    assert result['fragment'] == 'fragment'
    assert result['username'] is None
    assert result['password'] is None
    assert result['hostname'] == 'invalid_netloc'
    assert result['port'] is None
