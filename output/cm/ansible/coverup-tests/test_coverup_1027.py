# file lib/ansible/utils/collection_loader/_collection_finder.py:288-290
# lines [288, 290]
# branches []

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

# Mocking the _iter_modules_impl function
def mock_iter_modules_impl(paths, prefix):
    # This mock function will return a list of tuples with module name and ispkg flag
    return [("test_module", False)]

@pytest.fixture
def ansible_path_hook_finder(mocker):
    # Mock the _iter_modules_impl to return a controlled output
    mock = mocker.patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl', side_effect=mock_iter_modules_impl)
    # Create an instance of the _AnsiblePathHookFinder with a dummy collection_finder and pathctx
    finder = _AnsiblePathHookFinder(collection_finder=None, pathctx='/dummy/path')
    return finder, mock

def test_iter_modules(ansible_path_hook_finder):
    finder, mock_iter_modules_impl = ansible_path_hook_finder
    # Call the iter_modules method with a prefix
    modules = list(finder.iter_modules('dummy_prefix.'))
    # Assert that the mock function was called with the correct arguments
    mock_iter_modules_impl.assert_called_once_with(['/dummy/path'], 'dummy_prefix.')
    # Assert that the returned modules list matches the expected mock output
    assert modules == [("test_module", False)]
