# file: lib/ansible/galaxy/api.py:501-529
# asked: {"lines": [501, 502, 508, 509, 510, 511, 512, 513, 514, 518, 519, 521, 522, 523, 524, 525, 526, 527, 528, 529], "branches": [[521, 522], [521, 529]]}
# gained: {"lines": [501, 502, 508, 509, 510, 511, 512, 513, 514, 518, 519, 521, 522, 523, 524, 525, 526, 527, 528, 529], "branches": [[521, 522], [521, 529]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy=None, name='test', url='https://galaxy.ansible.com', available_api_versions={'v1': 'v1/'})

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api.display.warning')
def test_fetch_role_related_success(mock_warning, mock_call_galaxy, galaxy_api):
    mock_call_galaxy.side_effect = [
        {'results': [{'id': 1}], 'next_link': 'next_page'},
        {'results': [{'id': 2}], 'next_link': None}
    ]
    related = 'dependencies'
    role_id = 123
    results = galaxy_api.fetch_role_related(related, role_id)
    assert results == [{'id': 1}, {'id': 2}]
    mock_call_galaxy.assert_called()
    mock_warning.assert_not_called()

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api.display.warning')
def test_fetch_role_related_exception(mock_warning, mock_call_galaxy, galaxy_api):
    mock_call_galaxy.side_effect = Exception("Test exception")
    related = 'dependencies'
    role_id = 123
    results = galaxy_api.fetch_role_related(related, role_id)
    assert results == []
    mock_call_galaxy.assert_called()
    mock_warning.assert_called_once_with(
        "Unable to retrieve role (id=123) data (dependencies), but this is not fatal so we continue: Test exception"
    )
