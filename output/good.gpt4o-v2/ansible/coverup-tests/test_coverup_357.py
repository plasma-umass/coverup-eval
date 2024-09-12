# file: lib/ansible/galaxy/api.py:763-784
# asked: {"lines": [763, 764, 773, 774, 776, 777, 778, 779, 780, 782, 783, 784], "branches": []}
# gained: {"lines": [763, 764, 773, 774, 776, 777, 778, 779, 780, 782, 783, 784], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI, CollectionVersionMetadata

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy=None, name="GalaxyTest", url="https://galaxy.example.com")

def test_get_collection_version_metadata_v3(galaxy_api):
    namespace = "test_namespace"
    name = "test_name"
    version = "1.0.0"
    
    galaxy_api._available_api_versions = {'v3': 'api/v3', 'v2': 'api/v2'}
    galaxy_api.api_server = "https://galaxy.example.com"
    galaxy_api.name = "GalaxyTest"

    mock_data = {
        'namespace': {'name': namespace},
        'collection': {'name': name},
        'version': version,
        'download_url': 'https://galaxy.example.com/download/test_collection',
        'artifact': {'sha256': 'dummy_sha256'},
        'metadata': {'dependencies': {}}
    }

    with patch.object(galaxy_api, '_call_galaxy', return_value=mock_data) as mock_call_galaxy, \
         patch.object(galaxy_api, '_set_cache') as mock_set_cache:
        
        result = galaxy_api.get_collection_version_metadata(namespace, name, version)
        
        mock_call_galaxy.assert_called_once()
        mock_set_cache.assert_called_once()
        
        assert isinstance(result, CollectionVersionMetadata)
        assert result.namespace == namespace
        assert result.name == name
        assert result.version == version
        assert result.download_url == mock_data['download_url']
        assert result.artifact_sha256 == mock_data['artifact']['sha256']
        assert result.dependencies == mock_data['metadata']['dependencies']

def test_get_collection_version_metadata_v2(galaxy_api):
    namespace = "test_namespace"
    name = "test_name"
    version = "1.0.0"
    
    galaxy_api._available_api_versions = {'v2': 'api/v2'}
    galaxy_api.api_server = "https://galaxy.example.com"
    galaxy_api.name = "GalaxyTest"

    mock_data = {
        'namespace': {'name': namespace},
        'collection': {'name': name},
        'version': version,
        'download_url': 'https://galaxy.example.com/download/test_collection',
        'artifact': {'sha256': 'dummy_sha256'},
        'metadata': {'dependencies': {}}
    }

    with patch.object(galaxy_api, '_call_galaxy', return_value=mock_data) as mock_call_galaxy, \
         patch.object(galaxy_api, '_set_cache') as mock_set_cache:
        
        result = galaxy_api.get_collection_version_metadata(namespace, name, version)
        
        mock_call_galaxy.assert_called_once()
        mock_set_cache.assert_called_once()
        
        assert isinstance(result, CollectionVersionMetadata)
        assert result.namespace == namespace
        assert result.name == name
        assert result.version == version
        assert result.download_url == mock_data['download_url']
        assert result.artifact_sha256 == mock_data['artifact']['sha256']
        assert result.dependencies == mock_data['metadata']['dependencies']
