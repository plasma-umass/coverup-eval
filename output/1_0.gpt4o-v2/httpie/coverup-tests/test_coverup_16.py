# file: httpie/ssl.py:27-63
# asked: {"lines": [27, 28, 31, 32, 35, 36, 37, 38, 40, 42, 43, 44, 46, 47, 48, 50, 51, 53, 54, 56, 57, 58, 62], "branches": []}
# gained: {"lines": [27, 28, 31, 32, 35, 36, 37, 38, 40, 42, 43, 44, 46, 47, 48, 50, 51, 53, 54, 56, 57, 58, 62], "branches": []}

import pytest
import ssl
from httpie.ssl import HTTPieHTTPSAdapter
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from urllib3 import ProxyManager

@pytest.fixture
def adapter():
    return HTTPieHTTPSAdapter(verify=True, ssl_version='PROTOCOL_TLSv1_2', ciphers='ECDHE+AESGCM')

def test_init(adapter):
    assert isinstance(adapter, HTTPieHTTPSAdapter)
    assert isinstance(adapter._ssl_context, ssl.SSLContext)

def test_init_poolmanager(adapter, mocker):
    mock_super = mocker.patch.object(HTTPAdapter, 'init_poolmanager', return_value=None)
    adapter.init_poolmanager()
    mock_super.assert_called_once_with(ssl_context=adapter._ssl_context)

def test_proxy_manager_for(adapter, mocker):
    mock_super = mocker.patch.object(HTTPAdapter, 'proxy_manager_for', return_value=ProxyManager('http://proxy'))
    proxy_manager = adapter.proxy_manager_for()
    mock_super.assert_called_once_with(ssl_context=adapter._ssl_context)
    assert isinstance(proxy_manager, ProxyManager)

def test_create_ssl_context():
    context = HTTPieHTTPSAdapter._create_ssl_context(verify=True, ssl_version='PROTOCOL_TLSv1_2', ciphers='ECDHE+AESGCM')
    assert isinstance(context, ssl.SSLContext)
    assert context.verify_mode == ssl.CERT_REQUIRED

    context = HTTPieHTTPSAdapter._create_ssl_context(verify=False, ssl_version='PROTOCOL_TLSv1_2', ciphers='ECDHE+AESGCM')
    assert isinstance(context, ssl.SSLContext)
    assert context.verify_mode == ssl.CERT_NONE
