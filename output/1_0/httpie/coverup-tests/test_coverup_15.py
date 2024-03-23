# file httpie/ssl.py:27-63
# lines [27, 28, 31, 32, 35, 36, 37, 38, 40, 42, 43, 44, 46, 47, 48, 50, 51, 53, 54, 56, 57, 58, 62]
# branches []

import pytest
import ssl
from httpie.ssl import HTTPieHTTPSAdapter
from requests.adapters import HTTPAdapter

@pytest.fixture
def ssl_adapter():
    adapter = HTTPieHTTPSAdapter(verify=True)
    yield adapter
    adapter.close()

def test_httpie_https_adapter_init_poolmanager(ssl_adapter, mocker):
    mock_init_poolmanager = mocker.patch.object(HTTPAdapter, 'init_poolmanager')
    ssl_adapter.init_poolmanager(10, 10)
    assert ssl_adapter._ssl_context is not None
    mock_init_poolmanager.assert_called_once()

def test_httpie_https_adapter_proxy_manager_for(ssl_adapter, mocker):
    mock_proxy_manager_for = mocker.patch.object(HTTPAdapter, 'proxy_manager_for')
    ssl_adapter.proxy_manager_for('http://example.com')
    assert ssl_adapter._ssl_context is not None
    mock_proxy_manager_for.assert_called_once()

def test_httpie_https_adapter_create_ssl_context():
    context = HTTPieHTTPSAdapter._create_ssl_context(verify=True)
    assert context.verify_mode == ssl.CERT_REQUIRED

    context = HTTPieHTTPSAdapter._create_ssl_context(verify=False)
    assert context.verify_mode == ssl.CERT_NONE
