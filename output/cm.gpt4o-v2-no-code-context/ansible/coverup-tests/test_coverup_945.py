# file: lib/ansible/galaxy/api.py:555-583
# asked: {"lines": [558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 572, 573, 574, 576, 577, 579, 580, 582, 583], "branches": [[560, 561], [560, 563], [568, 569], [568, 572], [572, 573], [572, 576], [576, 577], [576, 579], [579, 580], [579, 582]]}
# gained: {"lines": [558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 572, 573, 574, 576, 577, 579, 580, 582, 583], "branches": [[560, 561], [560, 563], [568, 569], [568, 572], [572, 573], [572, 576], [576, 577], [576, 579], [579, 580], [579, 582]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    api = GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://example.com')
    api._available_api_versions = {'v1': 'v1'}
    api.api_server = 'http://example.com'
    return api

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_no_params(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    result = galaxy_api.search_roles(search=None)
    assert result == {'results': []}
    mock_call_galaxy.assert_called_once_with('http://example.com/v1/search/roles/?')

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_with_search(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    result = galaxy_api.search_roles(search='test')
    assert result == {'results': []}
    mock_call_galaxy.assert_called_once_with('http://example.com/v1/search/roles/?&autocomplete=test')

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_with_tags(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    result = galaxy_api.search_roles(search=None, tags='tag1,tag2')
    assert result == {'results': []}
    mock_call_galaxy.assert_called_once_with('http://example.com/v1/search/roles/?&tags_autocomplete=tag1+tag2')

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_with_platforms(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    result = galaxy_api.search_roles(search=None, platforms='platform1,platform2')
    assert result == {'results': []}
    mock_call_galaxy.assert_called_once_with('http://example.com/v1/search/roles/?&platforms_autocomplete=platform1+platform2')

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_with_page_size(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    result = galaxy_api.search_roles(search=None, page_size=10)
    assert result == {'results': []}
    mock_call_galaxy.assert_called_once_with('http://example.com/v1/search/roles/?&page_size=10')

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_with_author(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    result = galaxy_api.search_roles(search=None, author='author1')
    assert result == {'results': []}
    mock_call_galaxy.assert_called_once_with('http://example.com/v1/search/roles/?&username_autocomplete=author1')

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles_with_all_params(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}
    result = galaxy_api.search_roles(search='test', tags='tag1,tag2', platforms='platform1,platform2', page_size=10, author='author1')
    assert result == {'results': []}
    mock_call_galaxy.assert_called_once_with('http://example.com/v1/search/roles/?&autocomplete=test&tags_autocomplete=tag1+tag2&platforms_autocomplete=platform1+platform2&page_size=10&username_autocomplete=author1')
