# file lib/ansible/galaxy/api.py:501-529
# lines [501, 502, 508, 509, 510, 511, 512, 513, 514, 518, 519, 521, 522, 523, 524, 525, 526, 527, 528, 529]
# branches ['521->522', '521->529']

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    # Mocking the required arguments for GalaxyAPI initialization
    galaxy = MagicMock()
    name = 'test_name'
    url = 'http://example.com/api'
    api_instance = GalaxyAPI(galaxy, name, url)
    api_instance.api_server = url
    api_instance._available_api_versions = {'v1': 'v1'}
    return api_instance

@patch('ansible.galaxy.api._urljoin')
@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api.urlparse')
@patch('ansible.galaxy.api.display')
def test_fetch_role_related(mock_display, mock_urlparse, mock_call_galaxy, mock_urljoin, galaxy_api):
    # Setup
    role_id = '123'
    related = 'dependencies'
    api_server = 'http://example.com/api'
    galaxy_api.api_server = api_server

    # Mocking the URL join function
    mock_urljoin.side_effect = lambda *args: '/'.join(args)

    # Mocking the call to the Galaxy API
    mock_call_galaxy.side_effect = [
        {'results': [{'id': 1}], 'next_link': 'next_page'},
        {'results': [{'id': 2}], 'next_link': None}
    ]

    # Mocking the URL parse function
    mock_urlparse.return_value = MagicMock(scheme='http', netloc='example.com')

    # Execute
    results = galaxy_api.fetch_role_related(related, role_id)

    # Verify
    assert results == [{'id': 1}, {'id': 2}]
    mock_urljoin.assert_any_call(api_server, 'v1', 'roles', role_id, related, '?page_size=50')
    mock_urljoin.assert_any_call('http://example.com/', 'next_page')
    assert mock_call_galaxy.call_count == 2

    # Test exception handling
    mock_call_galaxy.side_effect = Exception("Test exception")
    results = galaxy_api.fetch_role_related(related, role_id)
    assert results == []
    mock_display.warning.assert_called_with(
        "Unable to retrieve role (id=123) data (dependencies), but this is not fatal so we continue: Test exception"
    )
