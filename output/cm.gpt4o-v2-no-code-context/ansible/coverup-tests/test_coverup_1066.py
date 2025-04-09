# file: lib/ansible/utils/collection_loader/_collection_config.py:90-93
# asked: {"lines": [92, 93], "branches": []}
# gained: {"lines": [92, 93], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

@pytest.fixture
def mock_collection_finder():
    with patch.object(_AnsibleCollectionConfig, '_collection_finder', create=True) as mock_finder:
        yield mock_finder

@pytest.fixture
def mock_require_finder():
    with patch.object(_AnsibleCollectionConfig, '_require_finder', create=True) as mock_require:
        yield mock_require

def test_playbook_paths(mock_collection_finder, mock_require_finder):
    # Setup the mock to return a specific value
    mock_collection_finder._n_playbook_paths = ['/path/to/playbook1', '/path/to/playbook2']
    
    # Access the property to trigger the code
    paths = _AnsibleCollectionConfig.playbook_paths.fget(_AnsibleCollectionConfig)
    
    # Assertions to verify the behavior
    assert paths == ['/path/to/playbook1', '/path/to/playbook2']
    mock_require_finder.assert_called_once()
