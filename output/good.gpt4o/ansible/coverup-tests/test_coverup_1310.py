# file lib/ansible/playbook/base.py:878-895
# lines []
# branches ['892->895']

import os
import pytest
from unittest.mock import Mock, patch
from ansible.playbook.base import Base

@pytest.fixture
def mock_base(mocker):
    base = Base()
    mocker.patch.object(base, 'get_dep_chain')
    mocker.patch.object(base, 'get_path')
    return base

def test_get_search_path_with_task_dir_not_in_path_stack(mock_base):
    # Mock the dependency chain to return an empty list
    mock_base.get_dep_chain.return_value = []
    
    # Mock the get_path method to return a specific path
    mock_base.get_path.return_value = '/some/path/to/task.yml'
    
    # Call the method under test
    search_path = mock_base.get_search_path()
    
    # Assert that the task directory is added to the path stack
    assert search_path == ['/some/path/to']

def test_get_search_path_with_task_dir_in_path_stack(mock_base):
    # Mock the dependency chain to return a list with a role path
    mock_role = Mock()
    mock_role._role_path = '/some/path/to'
    mock_base.get_dep_chain.return_value = [mock_role]
    
    # Mock the get_path method to return a path within the role path
    mock_base.get_path.return_value = '/some/path/to/task.yml'
    
    # Call the method under test
    search_path = mock_base.get_search_path()
    
    # Assert that the task directory is not added again to the path stack
    assert search_path == ['/some/path/to']
