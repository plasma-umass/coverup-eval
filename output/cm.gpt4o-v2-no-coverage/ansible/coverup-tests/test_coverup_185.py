# file: lib/ansible/galaxy/api.py:501-529
# asked: {"lines": [501, 502, 508, 509, 510, 511, 512, 513, 514, 518, 519, 521, 522, 523, 524, 525, 526, 527, 528, 529], "branches": [[521, 522], [521, 529]]}
# gained: {"lines": [501, 502, 508, 509, 510, 511, 512, 513, 514, 518, 519, 521, 522, 523, 524, 525, 526, 527, 528, 529], "branches": [[521, 522], [521, 529]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.six.moves.urllib.parse import urlparse
from ansible.module_utils._text import to_text
from ansible.galaxy.api import GalaxyAPI, _urljoin

@pytest.fixture
def galaxy_api():
    api = GalaxyAPI(
        galaxy=MagicMock(),
        name="test_name",
        url="https://galaxy.ansible.com/api",
        available_api_versions={'v1': 'v1'}
    )
    return api

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_fetch_role_related_success(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.side_effect = [
        {'results': [{'id': 1}], 'next_link': 'next_page'},
        {'results': [{'id': 2}], 'next_link': None}
    ]
    
    results = galaxy_api.fetch_role_related('dependencies', 123)
    
    assert results == [{'id': 1}, {'id': 2}]
    assert mock_call_galaxy.call_count == 2

@patch('ansible.galaxy.api.display.warning')
@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_fetch_role_related_exception(mock_call_galaxy, mock_warning, galaxy_api):
    mock_call_galaxy.side_effect = Exception("Test exception")
    
    results = galaxy_api.fetch_role_related('dependencies', 123)
    
    assert results == []
    mock_warning.assert_called_once_with("Unable to retrieve role (id=123) data (dependencies), but this is not fatal so we continue: Test exception")

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_fetch_role_related_no_next_link(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': [{'id': 1}], 'next_link': None}
    
    results = galaxy_api.fetch_role_related('dependencies', 123)
    
    assert results == [{'id': 1}]
    assert mock_call_galaxy.call_count == 1
