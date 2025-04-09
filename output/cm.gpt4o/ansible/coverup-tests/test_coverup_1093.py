# file lib/ansible/module_utils/urls.py:1034-1050
# lines [1035, 1036, 1037, 1039, 1041, 1042, 1043, 1044, 1046, 1048, 1049, 1050]
# branches ['1036->1037', '1036->1039', '1041->1042', '1041->1043', '1043->1044', '1043->1046', '1048->1049', '1048->1050']

import pytest
from unittest import mock
from ansible.module_utils.urls import SSLValidationHandler

@pytest.fixture
def ssl_validation_handler():
    handler = SSLValidationHandler(hostname='localhost', port=443)
    handler.ca_path = None
    return handler

def test_make_context_with_cafile(ssl_validation_handler):
    handler = ssl_validation_handler
    handler.ca_path = 'test_ca_path'
    
    with mock.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', True):
        with mock.patch('ansible.module_utils.urls.create_default_context') as mock_create_default_context:
            mock_context = mock.Mock()
            mock_create_default_context.return_value = mock_context
            
            context = handler.make_context('cafile', 'cadata')
            
            mock_create_default_context.assert_called_once_with(cafile='test_ca_path')
            assert context == mock_context
            mock_context.load_verify_locations.assert_called_once_with(cafile='test_ca_path', cadata=None)

def test_make_context_without_cafile(ssl_validation_handler):
    handler = ssl_validation_handler
    
    with mock.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', True):
        with mock.patch('ansible.module_utils.urls.create_default_context') as mock_create_default_context:
            mock_context = mock.Mock()
            mock_create_default_context.return_value = mock_context
            
            context = handler.make_context(None, 'cadata')
            
            mock_create_default_context.assert_called_once_with(cafile=None)
            assert context == mock_context
            mock_context.load_verify_locations.assert_called_once_with(cafile=None, cadata='cadata')

def test_make_context_no_sslcontext(ssl_validation_handler):
    handler = ssl_validation_handler
    
    with mock.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False):
        with mock.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False):
            with pytest.raises(NotImplementedError, match='Host libraries are too old to support creating an sslcontext'):
                handler.make_context(None, None)
