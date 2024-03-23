# file httpie/client.py:147-173
# lines [147, 149, 150, 152, 155, 156, 157, 159, 160, 163, 166, 167, 168, 169, 170, 173]
# branches ['166->167', '166->173']

import pytest
from httpie.client import build_requests_session
from httpie.plugins import TransportPlugin
from requests.adapters import HTTPAdapter

class MockTransportPlugin(TransportPlugin):
    prefix = 'mock://'

    def get_adapter(self):
        return HTTPAdapter()

@pytest.fixture
def plugin_manager(mocker):
    mock_plugin_manager = mocker.Mock()
    mock_plugin_manager.get_transport_plugins.return_value = [MockTransportPlugin]
    mocker.patch('httpie.client.plugin_manager', mock_plugin_manager)
    return mock_plugin_manager

def test_build_requests_session_with_plugin(mocker, plugin_manager):
    mocker.patch('httpie.client.AVAILABLE_SSL_VERSION_ARG_MAPPING', {'TLSv1.2': 'TLSv1_2'})
    session = build_requests_session(verify=False, ssl_version='TLSv1.2')
    assert session.adapters['https://'].__class__.__name__ == 'HTTPieHTTPSAdapter'
    assert session.adapters['mock://'].__class__.__name__ == 'HTTPAdapter'
    plugin_manager.get_transport_plugins.assert_called_once()
