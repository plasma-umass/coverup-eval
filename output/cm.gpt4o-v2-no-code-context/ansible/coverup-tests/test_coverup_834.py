# file: lib/ansible/utils/collection_loader/_collection_finder.py:488-489
# asked: {"lines": [488, 489], "branches": []}
# gained: {"lines": [488, 489], "branches": []}

import pytest
from unittest.mock import patch

# Assuming the class _AnsibleCollectionPkgLoaderBase is imported from the module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    
    @patch.object(_AnsibleCollectionPkgLoaderBase, '__init__', lambda self: None)
    def test_repr_with_subpackage_search_paths(self):
        # Create an instance of the class
        instance = _AnsibleCollectionPkgLoaderBase()
        instance._subpackage_search_paths = ['/mock/path']
        instance._source_code_path = '/mock/source/path'
        
        # Call the __repr__ method
        result = repr(instance)
        
        # Assert the expected result
        assert result == "_AnsibleCollectionPkgLoaderBase(path=['/mock/path'])"
    
    @patch.object(_AnsibleCollectionPkgLoaderBase, '__init__', lambda self: None)
    def test_repr_with_source_code_path(self):
        # Create an instance of the class
        instance = _AnsibleCollectionPkgLoaderBase()
        instance._subpackage_search_paths = None
        instance._source_code_path = '/mock/source/path'
        
        # Call the __repr__ method
        result = repr(instance)
        
        # Assert the expected result
        assert result == "_AnsibleCollectionPkgLoaderBase(path=/mock/source/path)"
