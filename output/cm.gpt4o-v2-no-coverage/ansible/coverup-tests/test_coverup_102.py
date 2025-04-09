# file: lib/ansible/galaxy/api.py:555-583
# asked: {"lines": [555, 556, 558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 572, 573, 574, 576, 577, 579, 580, 582, 583], "branches": [[560, 561], [560, 563], [568, 569], [568, 572], [572, 573], [572, 576], [576, 577], [576, 579], [579, 580], [579, 582]]}
# gained: {"lines": [555, 556, 558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 572, 573, 574, 576, 577, 579, 580, 582, 583], "branches": [[560, 561], [568, 569], [568, 572], [572, 573], [572, 576], [576, 577], [576, 579], [579, 580], [579, 582]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.six import string_types
from ansible.module_utils.six.moves.urllib.parse import quote as urlquote
from ansible.module_utils._text import to_bytes, to_text
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='galaxy', name='name', url='http://example.com', available_api_versions={'v1': 'v1/'})

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_search_roles(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': []}

    # Test with search parameter
    result = galaxy_api.search_roles('test_search')
    assert result == {'results': []}
    assert mock_call_galaxy.called
    assert 'autocomplete=test_search' in mock_call_galaxy.call_args[0][0]

    # Test with tags parameter
    result = galaxy_api.search_roles('test_search', tags='tag1,tag2')
    assert result == {'results': []}
    assert 'tags_autocomplete=tag1+tag2' in mock_call_galaxy.call_args[0][0]

    # Test with platforms parameter
    result = galaxy_api.search_roles('test_search', platforms='platform1,platform2')
    assert result == {'results': []}
    assert 'platforms_autocomplete=platform1+platform2' in mock_call_galaxy.call_args[0][0]

    # Test with page_size parameter
    result = galaxy_api.search_roles('test_search', page_size=10)
    assert result == {'results': []}
    assert 'page_size=10' in mock_call_galaxy.call_args[0][0]

    # Test with author parameter
    result = galaxy_api.search_roles('test_search', author='author1')
    assert result == {'results': []}
    assert 'username_autocomplete=author1' in mock_call_galaxy.call_args[0][0]

    # Test with all parameters
    result = galaxy_api.search_roles('test_search', tags='tag1,tag2', platforms='platform1,platform2', page_size=10, author='author1')
    assert result == {'results': []}
    assert 'autocomplete=test_search' in mock_call_galaxy.call_args[0][0]
    assert 'tags_autocomplete=tag1+tag2' in mock_call_galaxy.call_args[0][0]
    assert 'platforms_autocomplete=platform1+platform2' in mock_call_galaxy.call_args[0][0]
    assert 'page_size=10' in mock_call_galaxy.call_args[0][0]
    assert 'username_autocomplete=author1' in mock_call_galaxy.call_args[0][0]
