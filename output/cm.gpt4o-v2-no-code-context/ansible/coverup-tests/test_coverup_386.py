# file: lib/ansible/module_utils/urls.py:1120-1129
# asked: {"lines": [1120, 1121, 1122, 1123, 1124, 1129], "branches": [[1122, 0], [1122, 1123], [1123, 1124], [1123, 1129]]}
# gained: {"lines": [1120, 1121, 1122, 1123, 1124, 1129], "branches": [[1122, 0], [1122, 1123], [1123, 1124], [1123, 1129]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import maybe_add_ssl_handler, NoSSLError, SSLValidationHandler

def test_maybe_add_ssl_handler_https_with_validation_and_ssl(monkeypatch):
    url = 'https://example.com'
    validate_certs = True
    ca_path = '/path/to/ca'

    # Mocking HAS_SSL to be True
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSL', True)

    # Mocking SSLValidationHandler
    mock_ssl_handler = MagicMock()
    monkeypatch.setattr('ansible.module_utils.urls.SSLValidationHandler', mock_ssl_handler)

    handler = maybe_add_ssl_handler(url, validate_certs, ca_path)

    mock_ssl_handler.assert_called_once_with('example.com', 443, ca_path=ca_path)
    assert handler == mock_ssl_handler.return_value

def test_maybe_add_ssl_handler_https_with_validation_no_ssl(monkeypatch):
    url = 'https://example.com'
    validate_certs = True

    # Mocking HAS_SSL to be False
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSL', False)

    with pytest.raises(NoSSLError) as excinfo:
        maybe_add_ssl_handler(url, validate_certs)

    assert 'SSL validation is not available in your version of python' in str(excinfo.value)

def test_maybe_add_ssl_handler_https_without_validation(monkeypatch):
    url = 'https://example.com'
    validate_certs = False

    # Mocking SSLValidationHandler to ensure it is not called
    mock_ssl_handler = MagicMock()
    monkeypatch.setattr('ansible.module_utils.urls.SSLValidationHandler', mock_ssl_handler)

    handler = maybe_add_ssl_handler(url, validate_certs)

    mock_ssl_handler.assert_not_called()
    assert handler is None

def test_maybe_add_ssl_handler_non_https(monkeypatch):
    url = 'http://example.com'
    validate_certs = True

    # Mocking SSLValidationHandler to ensure it is not called
    mock_ssl_handler = MagicMock()
    monkeypatch.setattr('ansible.module_utils.urls.SSLValidationHandler', mock_ssl_handler)

    handler = maybe_add_ssl_handler(url, validate_certs)

    mock_ssl_handler.assert_not_called()
    assert handler is None
