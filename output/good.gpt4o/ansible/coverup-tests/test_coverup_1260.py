# file lib/ansible/module_utils/urls.py:853-882
# lines []
# branches ['863->874', '868->872', '879->882']

import pytest
from unittest import mock
from ansible.module_utils.urls import build_ssl_validation_error, SSLValidationError

# Mocking the necessary variables and functions
HAS_SSLCONTEXT = False
HAS_URLLIB3_PYOPENSSLCONTEXT = False
HAS_URLLIB3_SSL_WRAP_SOCKET = False

@mock.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', HAS_SSLCONTEXT)
@mock.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', HAS_URLLIB3_PYOPENSSLCONTEXT)
@mock.patch('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', HAS_URLLIB3_SSL_WRAP_SOCKET)
@mock.patch('sys.executable', '/usr/bin/python')
@mock.patch('sys.version', '2.7.8')
def test_build_ssl_validation_error(mocker):
    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs/ca-certificates.crt']
    exc = Exception('Test exception message')

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'the python executable used (/usr/bin/python) is version: 2.7.8' in str(excinfo.value)
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs/ca-certificates.crt.' in str(excinfo.value)
    assert 'The exception msg was: Test exception message.' in str(excinfo.value)

@mock.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', True)
@mock.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', True)
@mock.patch('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', True)
@mock.patch('sys.executable', '/usr/bin/python')
@mock.patch('sys.version', '2.7.8')
def test_build_ssl_validation_error_no_sslcontext(mocker):
    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs/ca-certificates.crt']
    exc = None

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs/ca-certificates.crt.' in str(excinfo.value)
