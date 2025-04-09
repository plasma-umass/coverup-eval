# file: lib/ansible/utils/collection_loader/_collection_finder.py:288-290
# asked: {"lines": [288, 290], "branches": []}
# gained: {"lines": [288, 290], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

# Assuming _AnsiblePathHookFinder is defined in ansible.utils.collection_loader._collection_finder
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture
def mock_iter_modules_impl(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl')

def test_iter_modules_executes(mock_iter_modules_impl):
    # Arrange
    collection_finder = MagicMock()
    pathctx = MagicMock()
    finder = _AnsiblePathHookFinder(collection_finder, pathctx)
    prefix = 'test_prefix'

    # Act
    result = finder.iter_modules(prefix)

    # Assert
    mock_iter_modules_impl.assert_called_once_with([finder._pathctx], prefix)
    assert result == mock_iter_modules_impl.return_value
