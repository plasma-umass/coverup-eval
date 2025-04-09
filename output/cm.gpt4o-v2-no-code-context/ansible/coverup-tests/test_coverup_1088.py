# file: lib/ansible/module_utils/urls.py:853-882
# asked: {"lines": [], "branches": [[863, 874], [868, 872]]}
# gained: {"lines": [], "branches": [[868, 872]]}

import pytest
import sys
from ansible.module_utils.urls import build_ssl_validation_error, SSLValidationError

# Mocking the constants to cover all branches
@pytest.fixture
def mock_constants(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)

@pytest.fixture
def mock_constants_partial(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', True)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)

def test_build_ssl_validation_error_no_sslcontext(mock_constants):
    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs/ca-certificates.crt']
    exc = None

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs/ca-certificates.crt.' in str(excinfo.value)

def test_build_ssl_validation_error_partial_sslcontext(mock_constants_partial):
    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs/ca-certificates.crt']
    exc = None

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs/ca-certificates.crt.' in str(excinfo.value)

def test_build_ssl_validation_error_with_exception(mock_constants):
    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs/ca-certificates.crt']
    exc = Exception('Test exception message')

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs/ca-certificates.crt.' in str(excinfo.value)
    assert 'The exception msg was: Test exception message.' in str(excinfo.value)
