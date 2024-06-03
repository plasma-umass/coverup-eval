# file lib/ansible/utils/collection_loader/_collection_finder.py:232-238
# lines [232, 234, 235, 236, 238]
# branches ['236->exit', '236->238']

import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

def test_ansible_path_hook_finder_initialization(mocker):
    # Mock the to_native function
    mock_to_native = mocker.patch('ansible.utils.collection_loader._collection_finder.to_native', return_value='mocked_pathctx')
    
    # Mock the collection_finder
    mock_collection_finder = mocker.Mock()
    
    # Mock the PY3 constant
    mocker.patch('ansible.utils.collection_loader._collection_finder.PY3', True)
    
    # Create an instance of _AnsiblePathHookFinder
    finder = _AnsiblePathHookFinder(mock_collection_finder, 'test_pathctx')
    
    # Assertions to verify the initialization
    mock_to_native.assert_called_once_with('test_pathctx')
    assert finder._pathctx == 'mocked_pathctx'
    assert finder._collection_finder == mock_collection_finder
    assert finder._file_finder is None
