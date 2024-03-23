# file lib/ansible/galaxy/api.py:555-583
# lines [558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 572, 573, 574, 576, 577, 579, 580, 582, 583]
# branches ['560->561', '560->563', '568->569', '568->572', '572->573', '572->576', '576->577', '576->579', '579->580', '579->582']

import pytest
from ansible.galaxy.api import GalaxyAPI
from ansible.module_utils.six.moves.urllib.parse import quote as urlquote
from ansible.module_utils._text import to_bytes, to_text
from unittest.mock import MagicMock

@pytest.fixture
def galaxy_api(mocker):
    api = GalaxyAPI("server", "username", "password")
    mocker.patch.object(api, '_call_galaxy', return_value={'available_versions': {'v1': 'v1/'}})
    mocker.patch.object(api, '_available_api_versions', {'v1': 'v1/'})
    return api

def test_search_roles_with_parameters(galaxy_api):
    search = "test_search"
    tags = "tag1,tag2"
    platforms = "platform1,platform2"
    page_size = 10
    author = "author_name"
    
    expected_url = (
        galaxy_api.api_server + "/v1/search/roles/?"
        "&autocomplete=" + to_text(urlquote(to_bytes(search))) +
        "&tags_autocomplete=" + '+'.join(tags.split(',')) +
        "&platforms_autocomplete=" + '+'.join(platforms.split(',')) +
        "&page_size=%s" % page_size +
        "&username_autocomplete=%s" % author
    )
    
    galaxy_api._call_galaxy = MagicMock(return_value="mocked_data")
    
    data = galaxy_api.search_roles(
        search=search,
        tags=tags,
        platforms=platforms,
        page_size=page_size,
        author=author
    )
    
    galaxy_api._call_galaxy.assert_called_once_with(expected_url)
    assert data == "mocked_data"
