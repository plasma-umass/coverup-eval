# file: lib/ansible/module_utils/urls.py:853-882
# asked: {"lines": [853, 858, 859, 863, 864, 866, 867, 868, 869, 872, 874, 879, 880, 882], "branches": [[863, 864], [863, 874], [868, 869], [868, 872], [879, 880], [879, 882]]}
# gained: {"lines": [853, 858, 859, 863, 864, 866, 867, 868, 869, 872, 874, 879, 880, 882], "branches": [[863, 864], [863, 874], [868, 869], [879, 880], [879, 882]]}

import pytest
import sys
from ansible.module_utils.urls import build_ssl_validation_error, SSLValidationError

def test_build_ssl_validation_error_no_sslcontext(monkeypatch):
    def mock_no_sslcontext():
        return False

    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', mock_no_sslcontext())
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', False)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', False)

    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs', '/usr/local/share/ca-certificates']
    exc = Exception('Test exception')

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'If the website serving the url uses SNI you need python >= 2.7.9 on your managed machine' in str(excinfo.value)
    assert 'the python executable used' in str(excinfo.value)
    assert 'or you can install the `urllib3`, `pyOpenSSL`, `ndg-httpsclient`, and `pyasn1` python modules' in str(excinfo.value)
    assert 'to perform SNI verification in python >= 2.6.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs, /usr/local/share/ca-certificates.' in str(excinfo.value)
    assert 'The exception msg was: Test exception.' in str(excinfo.value)

def test_build_ssl_validation_error_with_sslcontext(monkeypatch):
    def mock_with_sslcontext():
        return True

    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', mock_with_sslcontext())
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_PYOPENSSLCONTEXT', True)
    monkeypatch.setattr('ansible.module_utils.urls.HAS_URLLIB3_SSL_WRAP_SOCKET', True)

    hostname = 'example.com'
    port = 443
    paths = ['/etc/ssl/certs', '/usr/local/share/ca-certificates']
    exc = None

    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname, port, paths, exc)

    assert 'Failed to validate the SSL certificate for example.com:443.' in str(excinfo.value)
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity but this is unsafe and not recommended.' in str(excinfo.value)
    assert 'Paths checked for this platform: /etc/ssl/certs, /usr/local/share/ca-certificates.' in str(excinfo.value)
    assert 'The exception msg was:' not in str(excinfo.value)
