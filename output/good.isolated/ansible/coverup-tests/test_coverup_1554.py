# file lib/ansible/module_utils/urls.py:853-882
# lines [858, 859, 863, 864, 866, 867, 868, 869, 872, 874, 879, 880, 882]
# branches ['863->864', '863->874', '868->869', '868->872', '879->880', '879->882']

import pytest
import sys
from ansible.module_utils.urls import SSLValidationError, HAS_SSLCONTEXT, HAS_URLLIB3_PYOPENSSLCONTEXT, HAS_URLLIB3_SSL_WRAP_SOCKET
from ansible.module_utils._text import to_native

# Mocking sys.version_info to simulate the environment without SNI support
@pytest.fixture
def mock_sys_version_info(mocker):
    original_version_info = sys.version_info
    mocker.patch.object(sys, 'version_info', (2, 6, 9))
    mocker.patch.object(sys, 'executable', '/usr/bin/python')
    mocker.patch.object(sys, 'version', '2.6.9')
    yield
    sys.version_info = original_version_info

# Mocking the constants to simulate the environment without SNI support
@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)
    yield

def test_build_ssl_validation_error_without_sni_support(mock_sys_version_info, mock_constants):
    hostname = 'example.com'
    port = 443
    paths = ['/path/to/cert.pem']

    with pytest.raises(SSLValidationError) as exc_info:
        from ansible.module_utils.urls import build_ssl_validation_error
        build_ssl_validation_error(hostname, port, paths)

    exception_msg = str(exc_info.value)

    assert 'Failed to validate the SSL certificate for example.com:443.' in exception_msg
    assert 'Make sure your managed systems have a valid CA certificate installed.' in exception_msg
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in exception_msg
    assert 'the python executable used' in exception_msg
    assert 'is version: 2.6.9' in exception_msg
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in exception_msg
    assert 'to perform SNI verification in python >= 2.6.' in exception_msg
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in exception_msg
    assert 'Paths checked for this platform: /path/to/cert.pem.' in exception_msg
