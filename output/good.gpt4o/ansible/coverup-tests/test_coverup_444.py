# file lib/ansible/module_utils/urls.py:1120-1129
# lines [1120, 1121, 1122, 1123, 1124, 1129]
# branches ['1122->exit', '1122->1123', '1123->1124', '1123->1129']

import pytest
from unittest import mock
from ansible.module_utils.urls import maybe_add_ssl_handler, NoSSLError, SSLValidationHandler

def test_maybe_add_ssl_handler_https_with_validation(mocker):
    # Mocking the urlparse and generic_urlparse functions
    mocker.patch('ansible.module_utils.urls.urlparse', return_value=mock.Mock(scheme='https', hostname='example.com', port=None))
    mocker.patch('ansible.module_utils.urls.generic_urlparse', return_value=mock.Mock(scheme='https', hostname='example.com', port=None))
    
    # Mocking the HAS_SSL variable to True
    mocker.patch('ansible.module_utils.urls.HAS_SSL', True)
    
    # Call the function and assert the return type
    handler = maybe_add_ssl_handler('https://example.com', validate_certs=True)
    assert isinstance(handler, SSLValidationHandler)
    assert handler.hostname == 'example.com'
    assert handler.port == 443

def test_maybe_add_ssl_handler_https_without_ssl_support(mocker):
    # Mocking the urlparse and generic_urlparse functions
    mocker.patch('ansible.module_utils.urls.urlparse', return_value=mock.Mock(scheme='https', hostname='example.com', port=None))
    mocker.patch('ansible.module_utils.urls.generic_urlparse', return_value=mock.Mock(scheme='https', hostname='example.com', port=None))
    
    # Mocking the HAS_SSL variable to False
    mocker.patch('ansible.module_utils.urls.HAS_SSL', False)
    
    # Call the function and assert it raises NoSSLError
    with pytest.raises(NoSSLError):
        maybe_add_ssl_handler('https://example.com', validate_certs=True)

def test_maybe_add_ssl_handler_non_https(mocker):
    # Mocking the urlparse and generic_urlparse functions
    mocker.patch('ansible.module_utils.urls.urlparse', return_value=mock.Mock(scheme='http', hostname='example.com', port=None))
    mocker.patch('ansible.module_utils.urls.generic_urlparse', return_value=mock.Mock(scheme='http', hostname='example.com', port=None))
    
    # Call the function and assert it returns None
    handler = maybe_add_ssl_handler('http://example.com', validate_certs=True)
    assert handler is None
