# file: lib/ansible/module_utils/urls.py:1120-1129
# asked: {"lines": [1120, 1121, 1122, 1123, 1124, 1129], "branches": [[1122, 0], [1122, 1123], [1123, 1124], [1123, 1129]]}
# gained: {"lines": [1120, 1121, 1122, 1123, 1124, 1129], "branches": [[1122, 0], [1122, 1123], [1123, 1124], [1123, 1129]]}

import pytest
from ansible.module_utils.urls import maybe_add_ssl_handler, NoSSLError, SSLValidationHandler
from ansible.module_utils.six.moves.urllib.parse import urlparse

def test_maybe_add_ssl_handler_with_ssl(monkeypatch):
    def mock_generic_urlparse(url):
        class ParsedURL:
            scheme = 'https'
            hostname = 'example.com'
            port = 443
        return ParsedURL()
    
    monkeypatch.setattr('ansible.module_utils.urls.generic_urlparse', mock_generic_urlparse)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSL', True)
    
    handler = maybe_add_ssl_handler('https://example.com', True)
    assert isinstance(handler, SSLValidationHandler)
    assert handler.hostname == 'example.com'
    assert handler.port == 443

def test_maybe_add_ssl_handler_without_ssl(monkeypatch):
    def mock_generic_urlparse(url):
        class ParsedURL:
            scheme = 'https'
            hostname = 'example.com'
            port = 443
        return ParsedURL()
    
    monkeypatch.setattr('ansible.module_utils.urls.generic_urlparse', mock_generic_urlparse)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSL', False)
    
    with pytest.raises(NoSSLError):
        maybe_add_ssl_handler('https://example.com', True)

def test_maybe_add_ssl_handler_non_https(monkeypatch):
    def mock_generic_urlparse(url):
        class ParsedURL:
            scheme = 'http'
            hostname = 'example.com'
            port = 80
        return ParsedURL()
    
    monkeypatch.setattr('ansible.module_utils.urls.generic_urlparse', mock_generic_urlparse)
    
    handler = maybe_add_ssl_handler('http://example.com', True)
    assert handler is None
