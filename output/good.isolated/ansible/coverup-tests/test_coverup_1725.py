# file lib/ansible/utils/collection_loader/_collection_finder.py:485-486
# lines [486]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_finder

# Assuming _iter_modules_impl is a function that needs to be tested for coverage
# and _subpackage_search_paths is an attribute of the _AnsibleCollectionPkgLoaderBase class.

# Mocking the _iter_modules_impl function to track its call
def test_iter_modules_calls_iter_modules_impl(mocker):
    # Arrange
    mock_iter_modules_impl = mocker.patch(
        'ansible.utils.collection_loader._collection_finder._iter_modules_impl',
        return_value=iter([])
    )
    # Mocking the __init__ method to not require the 'fullname' argument
    mocker.patch.object(
        _collection_finder._AnsibleCollectionPkgLoaderBase,
        '__init__',
        return_value=None
    )
    loader = _collection_finder._AnsibleCollectionPkgLoaderBase()
    loader._subpackage_search_paths = ['some/path']
    prefix = 'some_prefix'

    # Act
    list(loader.iter_modules(prefix))

    # Assert
    mock_iter_modules_impl.assert_called_once_with(loader._subpackage_search_paths, prefix)
