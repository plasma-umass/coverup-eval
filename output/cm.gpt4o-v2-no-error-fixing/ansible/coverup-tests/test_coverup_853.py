# file: lib/ansible/module_utils/urls.py:853-882
# asked: {"lines": [], "branches": [[863, 874], [868, 872]]}
# gained: {"lines": [], "branches": [[868, 872]]}

import pytest
import sys
from ansible.module_utils.urls import build_ssl_validation_error, SSLValidationError

def test_build_ssl_validation_error_no_sslcontext_no_urllib3(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)

    hostname = 'example.com'
    port = 443
    paths = ['/path/to/cert']

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /path/to/cert.' in str(excinfo.value)

def test_build_ssl_validation_error_no_sslcontext_with_urllib3(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', True)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', True)

    hostname = 'example.com'
    port = 443
    paths = ['/path/to/cert']

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /path/to/cert.' in str(excinfo.value)

def test_build_ssl_validation_error_with_exception(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)

    hostname = 'example.com'
    port = 443
    paths = ['/path/to/cert']
    exception_message = 'Test exception'

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc=exception_message)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /path/to/cert.' in str(excinfo.value)
    assert 'The exception msg was: Test exception.' in str(excinfo.value)
