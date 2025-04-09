# file: lib/ansible/playbook/base.py:878-895
# asked: {"lines": [878, 883, 885, 887, 888, 891, 892, 893, 895], "branches": [[887, 888], [887, 891], [892, 893], [892, 895]]}
# gained: {"lines": [878, 883, 885, 887, 888, 891, 892, 893, 895], "branches": [[887, 888], [887, 891], [892, 893], [892, 895]]}

import pytest
import os
from unittest.mock import MagicMock

class TestBase:
    @pytest.fixture
    def base(self):
        from ansible.playbook.base import Base
        return Base()

    def test_get_search_path_with_dep_chain(self, mocker, base):
        # Mocking get_dep_chain to return a list of objects with _role_path attribute
        mock_dep_chain = [MagicMock(_role_path='/path/to/role1'), MagicMock(_role_path='/path/to/role2')]
        mocker.patch.object(base, 'get_dep_chain', return_value=mock_dep_chain)
        
        # Mocking get_path to return a path
        mocker.patch.object(base, 'get_path', return_value='/path/to/task/file.yml')
        
        expected_path_stack = ['/path/to/role2', '/path/to/role1', '/path/to/task']
        
        assert base.get_search_path() == expected_path_stack

    def test_get_search_path_without_dep_chain(self, mocker, base):
        # Mocking get_dep_chain to return None
        mocker.patch.object(base, 'get_dep_chain', return_value=None)
        
        # Mocking get_path to return a path
        mocker.patch.object(base, 'get_path', return_value='/path/to/task/file.yml')
        
        expected_path_stack = ['/path/to/task']
        
        assert base.get_search_path() == expected_path_stack

    def test_get_search_path_task_dir_in_dep_chain(self, mocker, base):
        # Mocking get_dep_chain to return a list of objects with _role_path attribute
        mock_dep_chain = [MagicMock(_role_path='/path/to/task')]
        mocker.patch.object(base, 'get_dep_chain', return_value=mock_dep_chain)
        
        # Mocking get_path to return a path
        mocker.patch.object(base, 'get_path', return_value='/path/to/task/file.yml')
        
        expected_path_stack = ['/path/to/task']
        
        assert base.get_search_path() == expected_path_stack
