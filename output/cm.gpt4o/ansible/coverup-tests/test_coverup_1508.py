# file lib/ansible/module_utils/urls.py:853-882
# lines []
# branches ['868->872']

import pytest
from ansible.module_utils.urls import build_ssl_validation_error, SSLValidationError

def test_build_ssl_validation_error_no_sslcontext(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)
    mocker.patch('sys.executable', '/usr/bin/python')
    mocker.patch('sys.version', '2.7.5')

    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs', '/usr/local/share/ca-certificates']

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'the python executable used (/usr/bin/python) is version: 2.7.5' in str(excinfo.value)
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs, /usr/local/share/ca-certificates.' in str(excinfo.value)

def test_build_ssl_validation_error_partial_sslcontext(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', True)
    mocker.patch('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)
    mocker.patch('sys.executable', '/usr/bin/python')
    mocker.patch('sys.version', '2.7.5')

    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs', '/usr/local/share/ca-certificates']

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'the python executable used (/usr/bin/python) is version: 2.7.5' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs, /usr/local/share/ca-certificates.' in str(excinfo.value)
