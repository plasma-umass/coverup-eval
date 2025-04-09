# file httpie/client.py:147-173
# lines [147, 149, 150, 152, 155, 156, 157, 159, 160, 163, 166, 167, 168, 169, 170, 173]
# branches ['166->167', '166->173']

import pytest
import requests
from unittest.mock import patch, MagicMock
from httpie.client import build_requests_session, HTTPieHTTPSAdapter, plugin_manager

def test_build_requests_session(mocker):
    # Mock the HTTPieHTTPSAdapter and plugin_manager
    mock_https_adapter = mocker.patch('httpie.client.HTTPieHTTPSAdapter', autospec=True)
    mock_plugin_manager = mocker.patch('httpie.client.plugin_manager', autospec=True)
    
    # Mock the AVAILABLE_SSL_VERSION_ARG_MAPPING
    mock_ssl_version_mapping = mocker.patch('httpie.client.AVAILABLE_SSL_VERSION_ARG_MAPPING', autospec=True)
    mock_ssl_version_mapping.__getitem__.return_value = 'mocked_ssl_version'
    
    # Mock the return value of get_transport_plugins
    mock_plugin_cls = MagicMock()
    mock_plugin_instance = MagicMock()
    mock_plugin_instance.prefix = 'mock://'
    mock_plugin_instance.get_adapter.return_value = MagicMock()
    mock_plugin_cls.return_value = mock_plugin_instance
    mock_plugin_manager.get_transport_plugins.return_value = [mock_plugin_cls]
    
    # Call the function with test parameters
    session = build_requests_session(verify=True, ssl_version='TLSv1.2', ciphers='ECDHE-RSA-AES128-GCM-SHA256')
    
    # Assertions to verify the correct behavior
    mock_https_adapter.assert_called_once_with(
        ciphers='ECDHE-RSA-AES128-GCM-SHA256',
        verify=True,
        ssl_version='mocked_ssl_version'
    )
    assert session.adapters['https://'] == mock_https_adapter.return_value
    assert session.adapters['mock://'] == mock_plugin_instance.get_adapter.return_value

    # Clean up
    mocker.stopall()
