# file: lib/ansible/module_utils/urls.py:1120-1129
# asked: {"lines": [1120, 1121, 1122, 1123, 1124, 1129], "branches": [[1122, 0], [1122, 1123], [1123, 1124], [1123, 1129]]}
# gained: {"lines": [1120, 1121, 1122, 1123, 1124, 1129], "branches": [[1122, 0], [1122, 1123], [1123, 1124], [1123, 1129]]}

import pytest
from ansible.module_utils.urls import maybe_add_ssl_handler, NoSSLError, SSLValidationHandler
from ansible.module_utils.six.moves.urllib.parse import urlparse

def test_maybe_add_ssl_handler_with_ssl(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSL', True)
    url = 'https://example.com'
    validate_certs = True
    ca_path = '/path/to/ca'

    handler = maybe_add_ssl_handler(url, validate_certs, ca_path)
    assert isinstance(handler, SSLValidationHandler)
    assert handler.hostname == 'example.com'
    assert handler.port == 443
    assert handler.ca_path == ca_path

def test_maybe_add_ssl_handler_without_ssl(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSL', False)
    url = 'https://example.com'
    validate_certs = True

    with pytest.raises(NoSSLError):
        maybe_add_ssl_handler(url, validate_certs)

def test_maybe_add_ssl_handler_http_url(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSL', True)
    url = 'http://example.com'
    validate_certs = True

    handler = maybe_add_ssl_handler(url, validate_certs)
    assert handler is None
