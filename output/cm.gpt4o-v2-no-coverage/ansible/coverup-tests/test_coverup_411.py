# file: lib/ansible/galaxy/api.py:763-784
# asked: {"lines": [763, 764, 773, 774, 776, 777, 778, 779, 780, 782, 783, 784], "branches": []}
# gained: {"lines": [763, 764, 773, 774, 776, 777, 778, 779, 780, 782, 783, 784], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI, CollectionVersionMetadata

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(
        galaxy=MagicMock(),
        name="test_galaxy",
        url="https://galaxy.example.com",
        available_api_versions={"v2": "api/v2", "v3": "api/v3"}
    )

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api.GalaxyAPI._set_cache')
def test_get_collection_version_metadata(mock_set_cache, mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {
        'namespace': {'name': 'test_namespace'},
        'collection': {'name': 'test_collection'},
        'version': '1.0.0',
        'download_url': 'https://example.com/download',
        'artifact': {'sha256': 'dummy_sha256'},
        'metadata': {'dependencies': {}}
    }

    result = galaxy_api.get_collection_version_metadata('test_namespace', 'test_collection', '1.0.0')

    mock_call_galaxy.assert_called_once()
    mock_set_cache.assert_called_once()
    
    assert isinstance(result, CollectionVersionMetadata)
    assert result.namespace == 'test_namespace'
    assert result.name == 'test_collection'
    assert result.version == '1.0.0'
    assert result.download_url == 'https://example.com/download'
    assert result.artifact_sha256 == 'dummy_sha256'
    assert result.dependencies == {}
