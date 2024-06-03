# file lib/ansible/utils/collection_loader/_collection_finder.py:485-486
# lines [485, 486]
# branches []

import pytest
from unittest.mock import patch

# Assuming _iter_modules_impl is a function in the same module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_iter_modules_impl(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl')

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        self._subpackage_search_paths = []

def test_iter_modules(mock_iter_modules_impl):
    # Arrange
    loader = MockAnsibleCollectionPkgLoaderBase()
    loader._subpackage_search_paths = ['path1', 'path2']
    prefix = 'test_prefix'
    expected_result = ['module1', 'module2']
    mock_iter_modules_impl.return_value = expected_result

    # Act
    result = loader.iter_modules(prefix)

    # Assert
    mock_iter_modules_impl.assert_called_once_with(loader._subpackage_search_paths, prefix)
    assert result == expected_result
