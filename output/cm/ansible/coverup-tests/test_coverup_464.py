# file lib/ansible/module_utils/urls.py:1120-1129
# lines [1120, 1121, 1122, 1123, 1124, 1129]
# branches ['1122->exit', '1122->1123', '1123->1124', '1123->1129']

import pytest
from ansible.module_utils.urls import maybe_add_ssl_handler, SSLValidationHandler, NoSSLError
from ansible.module_utils.urls import HAS_SSL

@pytest.fixture
def ssl_handler_mock(mocker):
    return mocker.patch('ansible.module_utils.urls.SSLValidationHandler', autospec=True)

def test_maybe_add_ssl_handler_with_https_and_validation(mocker, ssl_handler_mock):
    mocker.patch('ansible.module_utils.urls.HAS_SSL', True)

    url = 'https://example.com'
    validate_certs = True
    ca_path = '/path/to/ca'

    handler = maybe_add_ssl_handler(url, validate_certs, ca_path=ca_path)

    ssl_handler_mock.assert_called_once_with('example.com', 443, ca_path=ca_path)
    assert isinstance(handler, SSLValidationHandler)

def test_maybe_add_ssl_handler_without_ssl_module(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSL', False)

    url = 'https://example.com'
    validate_certs = True

    with pytest.raises(NoSSLError) as excinfo:
        maybe_add_ssl_handler(url, validate_certs)

    assert 'SSL validation is not available in your version of python' in str(excinfo.value)
