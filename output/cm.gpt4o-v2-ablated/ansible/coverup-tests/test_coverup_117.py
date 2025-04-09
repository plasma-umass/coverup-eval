# file: lib/ansible/playbook/base.py:878-895
# asked: {"lines": [878, 883, 885, 887, 888, 891, 892, 893, 895], "branches": [[887, 888], [887, 891], [892, 893], [892, 895]]}
# gained: {"lines": [878, 883, 885, 887, 888, 891, 892, 893, 895], "branches": [[887, 888], [887, 891], [892, 893], [892, 895]]}

import os
import pytest
from unittest.mock import MagicMock

# Assuming the Base class is imported from ansible.playbook.base
from ansible.playbook.base import Base

class TestBase:
    @pytest.fixture
    def base_instance(self, mocker):
        instance = Base()
        mocker.patch.object(instance, 'get_dep_chain')
        mocker.patch.object(instance, 'get_path')
        return instance

    def test_get_search_path_with_dep_chain(self, base_instance):
        # Mocking the dependency chain with _role_path attributes
        dep_chain = [MagicMock(_role_path='/path/to/role1'), MagicMock(_role_path='/path/to/role2')]
        base_instance.get_dep_chain.return_value = dep_chain
        base_instance.get_path.return_value = '/path/to/task/file.yml'

        expected_path_stack = ['/path/to/role2', '/path/to/role1', '/path/to/task']
        result = base_instance.get_search_path()

        assert result == expected_path_stack

    def test_get_search_path_without_dep_chain(self, base_instance):
        # Mocking an empty dependency chain
        base_instance.get_dep_chain.return_value = []
        base_instance.get_path.return_value = '/path/to/task/file.yml'

        expected_path_stack = ['/path/to/task']
        result = base_instance.get_search_path()

        assert result == expected_path_stack

    def test_get_search_path_task_dir_in_dep_chain(self, base_instance):
        # Mocking the dependency chain with _role_path attributes including task dir
        dep_chain = [MagicMock(_role_path='/path/to/task'), MagicMock(_role_path='/path/to/role2')]
        base_instance.get_dep_chain.return_value = dep_chain
        base_instance.get_path.return_value = '/path/to/task/file.yml'

        expected_path_stack = ['/path/to/role2', '/path/to/task']
        result = base_instance.get_search_path()

        assert result == expected_path_stack
