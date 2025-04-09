# file: lib/ansible/utils/collection_loader/_collection_finder.py:485-486
# asked: {"lines": [486], "branches": []}
# gained: {"lines": [486], "branches": []}

import pytest
from unittest.mock import patch

# Assuming _iter_modules_impl is a function in the same module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase, _iter_modules_impl

class TestAnsibleCollectionPkgLoaderBase:
    
    @patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl')
    def test_iter_modules(self, mock_iter_modules_impl):
        # Arrange
        class TestLoader(_AnsibleCollectionPkgLoaderBase):
            def __init__(self):
                self._subpackage_search_paths = ['path1', 'path2']
        
        loader = TestLoader()
        prefix = 'test_prefix'
        
        # Act
        result = loader.iter_modules(prefix)
        
        # Assert
        mock_iter_modules_impl.assert_called_once_with(loader._subpackage_search_paths, prefix)
        assert result == mock_iter_modules_impl.return_value
