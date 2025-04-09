# file lib/ansible/playbook/base.py:878-895
# lines [878, 883, 885, 887, 888, 891, 892, 893, 895]
# branches ['887->888', '887->891', '892->893', '892->895']

import os
import pytest
from ansible.playbook.base import Base
from unittest.mock import Mock

# Mock the Base class to test get_search_path method
class MockBase(Base):
    def __init__(self, dep_chain=None, path=None):
        self._dep_chain = dep_chain
        self._path = path

    def get_dep_chain(self):
        return self._dep_chain

    def get_path(self):
        return self._path

@pytest.fixture
def mock_os_path_dirname(mocker):
    mock = mocker.patch('os.path.dirname')
    mock.return_value = '/path/to/task'
    return mock

def test_get_search_path_with_dep_chain_and_unique_task_dir(mock_os_path_dirname):
    # Create a mock dependency chain with role paths
    dep_chain = [
        Mock(_role_path='/path/to/role1'),
        Mock(_role_path='/path/to/role2'),
    ]
    # Create a MockBase instance with the mock dependency chain and a unique task path
    base = MockBase(dep_chain=dep_chain, path='/path/to/unique/task/main.yml')

    # Call the method under test
    search_path = base.get_search_path()

    # Assert that the search path contains the reversed dependency chain and the task dir
    assert search_path == ['/path/to/role2', '/path/to/role1', '/path/to/task']

def test_get_search_path_without_dep_chain(mock_os_path_dirname):
    # Create a MockBase instance with no dependency chain and a task path
    base = MockBase(dep_chain=None, path='/path/to/task/main.yml')

    # Call the method under test
    search_path = base.get_search_path()

    # Assert that the search path only contains the task dir
    assert search_path == ['/path/to/task']

def test_get_search_path_with_dep_chain_and_existing_task_dir(mock_os_path_dirname):
    # Create a mock dependency chain with role paths, including the task dir
    dep_chain = [
        Mock(_role_path='/path/to/role1'),
        Mock(_role_path='/path/to/task'),
    ]
    # Create a MockBase instance with the mock dependency chain and a task path that is already in the dep chain
    base = MockBase(dep_chain=dep_chain, path='/path/to/task/main.yml')

    # Call the method under test
    search_path = base.get_search_path()

    # Assert that the search path contains the reversed dependency chain without duplicate task dir
    assert search_path == ['/path/to/task', '/path/to/role1']
