# file lib/ansible/utils/collection_loader/_collection_finder.py:110-128
# lines [110, 111, 112, 113, 114, 117, 118, 119, 122, 124, 127, 128]
# branches ['112->113', '112->117', '113->112', '113->114', '117->118', '117->122', '118->117', '118->119', '127->exit', '127->128']

import sys
import pytest
from ansible.utils.collection_loader import _collection_finder

class TestAnsibleCollectionFinder:
    @pytest.fixture
    def finder(self, mocker):
        # Create a mock _AnsibleCollectionFinder instance
        finder = mocker.MagicMock(spec=_collection_finder._AnsibleCollectionFinder)
        # Add the mock to sys.meta_path
        sys.meta_path.append(finder)
        # Create a mock path hook with the finder as __self__
        path_hook = mocker.MagicMock()
        path_hook.__self__ = finder
        # Add the mock path hook to sys.path_hooks
        sys.path_hooks.append(path_hook)
        # Set a mock collection_finder in AnsibleCollectionConfig
        _collection_finder.AnsibleCollectionConfig._collection_finder = finder
        yield finder
        # Cleanup after the test
        if finder in sys.meta_path:
            sys.meta_path.remove(finder)
        if path_hook in sys.path_hooks:
            sys.path_hooks.remove(path_hook)
        _collection_finder.AnsibleCollectionConfig._collection_finder = None
        sys.path_importer_cache.clear()

    def test_remove(self, finder):
        # Ensure the finder is in the meta_path
        assert finder in sys.meta_path
        # Ensure the mock path hook is in sys.path_hooks
        assert any(hasattr(ph, '__self__') and ph.__self__ is finder for ph in sys.path_hooks)
        assert _collection_finder.AnsibleCollectionConfig._collection_finder is not None

        # Call the remove method
        _collection_finder._AnsibleCollectionFinder._remove()

        # Assert the finder is removed from meta_path
        assert finder not in sys.meta_path
        # Assert the mock path hook is removed from sys.path_hooks
        assert not any(hasattr(ph, '__self__') and ph.__self__ is finder for ph in sys.path_hooks)
        # Assert the collection_finder is set to None
        assert _collection_finder.AnsibleCollectionConfig._collection_finder is None
        # Assert the public property is None
        assert _collection_finder.AnsibleCollectionConfig.collection_finder is None
