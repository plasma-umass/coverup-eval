# file lib/ansible/module_utils/urls.py:1034-1050
# lines [1037, 1043, 1044, 1046, 1049]
# branches ['1036->1037', '1041->1043', '1043->1044', '1043->1046', '1048->1049']

import pytest
from ansible.module_utils.urls import SSLValidationHandler
from unittest.mock import patch, MagicMock

# Mocking constants to force different branches to execute
@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)

def test_ssl_validation_handler_no_sslcontext_no_pyopenssl(mock_constants):
    handler = SSLValidationHandler(hostname='fakehost', port=443)
    handler.ca_path = '/fake/path'

    with pytest.raises(NotImplementedError) as excinfo:
        handler.make_context(cafile=None, cadata=None)
    assert 'Host libraries are too old to support creating an sslcontext' in str(excinfo.value)

def test_ssl_validation_handler_with_ca_path():
    handler = SSLValidationHandler(hostname='fakehost', port=443)
    handler.ca_path = '/fake/path'

    with patch('ansible.module_utils.urls.create_default_context') as mock_create_default_context:
        mock_create_default_context.return_value = MagicMock()
        context = handler.make_context(cafile=None, cadata='fake_cadata')
        mock_create_default_context.assert_called_once_with(cafile='/fake/path')
        assert context is not None

def test_ssl_validation_handler_with_cadata():
    handler = SSLValidationHandler(hostname='fakehost', port=443)
    handler.ca_path = None

    with patch('ansible.module_utils.urls.create_default_context') as mock_create_default_context:
        mock_create_default_context.return_value = MagicMock()
        context = handler.make_context(cafile=None, cadata='fake_cadata')
        mock_create_default_context.assert_called_once_with(cafile=None)
        assert context is not None
