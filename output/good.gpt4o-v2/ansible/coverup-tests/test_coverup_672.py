# file: lib/ansible/utils/collection_loader/_collection_finder.py:130-136
# asked: {"lines": [130, 131, 132, 134, 136], "branches": []}
# gained: {"lines": [130, 131, 132, 134, 136], "branches": []}

import pytest
import sys
from unittest.mock import MagicMock, patch
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
from ansible.utils.collection_loader._collection_config import AnsibleCollectionConfig

@pytest.fixture
def setup_finder():
    finder = _AnsibleCollectionFinder()
    original_finder = AnsibleCollectionConfig._collection_finder
    yield finder
    # Cleanup
    if finder in sys.meta_path:
        sys.meta_path.remove(finder)
    if finder._ansible_collection_path_hook in sys.path_hooks:
        sys.path_hooks.remove(finder._ansible_collection_path_hook)
    AnsibleCollectionConfig._collection_finder = original_finder
    AnsibleCollectionConfig.collection_finder = original_finder

def test_install_method(setup_finder):
    finder = setup_finder

    # Mock the _remove method
    with patch.object(finder, '_remove', return_value=None) as mock_remove:
        # Mock the _ansible_collection_path_hook attribute
        finder._ansible_collection_path_hook = MagicMock()

        # Call the _install method
        finder._install()

        # Assertions
        mock_remove.assert_called_once()
        assert sys.meta_path[0] == finder
        assert sys.path_hooks[0] == finder._ansible_collection_path_hook
        assert AnsibleCollectionConfig.collection_finder == finder
