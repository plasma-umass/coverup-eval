# file: lib/ansible/module_utils/urls.py:853-882
# asked: {"lines": [], "branches": [[868, 872]]}
# gained: {"lines": [], "branches": [[868, 872]]}

import pytest
from ansible.module_utils.urls import build_ssl_validation_error, SSLValidationError

def test_build_ssl_validation_error_no_sslcontext_no_urllib3(monkeypatch):
    def mock_has_sslcontext():
        return False

    def mock_has_urllib3_pyopensslcontext():
        return False

    def mock_has_urllib3_ssl_wrap_socket():
        return False

    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', mock_has_sslcontext())
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', mock_has_urllib3_pyopensslcontext())
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', mock_has_urllib3_ssl_wrap_socket())

    hostname = 'example.com'
    port = 443
    paths = ['/path/to/cert']

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths)

    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)

def test_build_ssl_validation_error_no_sslcontext_with_urllib3(monkeypatch):
    def mock_has_sslcontext():
        return False

    def mock_has_urllib3_pyopensslcontext():
        return True

    def mock_has_urllib3_ssl_wrap_socket():
        return True

    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', mock_has_sslcontext())
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', mock_has_urllib3_pyopensslcontext())
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', mock_has_urllib3_ssl_wrap_socket())

    hostname = 'example.com'
    port = 443
    paths = ['/path/to/cert']

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths)

    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
