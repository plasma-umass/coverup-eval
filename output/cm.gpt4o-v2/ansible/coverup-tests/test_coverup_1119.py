# file: lib/ansible/galaxy/api.py:555-583
# asked: {"lines": [558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 572, 573, 574, 576, 577, 579, 580, 582, 583], "branches": [[560, 561], [560, 563], [568, 569], [568, 572], [572, 573], [572, 576], [576, 577], [576, 579], [579, 580], [579, 582]]}
# gained: {"lines": [558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 572, 573, 574, 576, 577, 579, 580, 582, 583], "branches": [[560, 561], [560, 563], [568, 569], [568, 572], [572, 573], [572, 576], [576, 577], [576, 579], [579, 580], [579, 582]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='galaxy', name='name', url='http://example.com', available_api_versions={'v1': 'v1'})

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_all_params(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    
    search = 'test_search'
    tags = 'tag1,tag2'
    platforms = 'platform1,platform2'
    page_size = 10
    author = 'test_author'
    
    result = galaxy_api.search_roles(search, tags=tags, platforms=platforms, page_size=page_size, author=author)
    
    expected_url = (
        f"{galaxy_api.api_server}/{galaxy_api.available_api_versions['v1']}/search/roles/?"
        f"&autocomplete={search}"
        f"&tags_autocomplete=tag1+tag2"
        f"&platforms_autocomplete=platform1+platform2"
        f"&page_size={page_size}"
        f"&username_autocomplete={author}"
    )
    
    mock_call_galaxy.assert_called_once_with(expected_url)
    assert result == {'results': []}

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_no_params(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    
    result = galaxy_api.search_roles(None)
    
    expected_url = f"{galaxy_api.api_server}/{galaxy_api.available_api_versions['v1']}/search/roles/?"
    
    mock_call_galaxy.assert_called_once_with(expected_url)
    assert result == {'results': []}

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_some_params(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    
    search = 'test_search'
    tags = 'tag1,tag2'
    
    result = galaxy_api.search_roles(search, tags=tags)
    
    expected_url = (
        f"{galaxy_api.api_server}/{galaxy_api.available_api_versions['v1']}/search/roles/?"
        f"&autocomplete={search}"
        f"&tags_autocomplete=tag1+tag2"
    )
    
    mock_call_galaxy.assert_called_once_with(expected_url)
    assert result == {'results': []}
