# file: lib/ansible/playbook/base.py:878-895
# asked: {"lines": [878, 883, 885, 887, 888, 891, 892, 893, 895], "branches": [[887, 888], [887, 891], [892, 893], [892, 895]]}
# gained: {"lines": [878, 883, 885, 887, 888, 891, 892, 893, 895], "branches": [[887, 888], [887, 891], [892, 893], [892, 895]]}

import pytest
import os
from unittest.mock import MagicMock, patch
from ansible.playbook.base import Base

class MockRole:
    def __init__(self, role_path):
        self._role_path = role_path

@pytest.fixture
def mock_base(monkeypatch):
    base_instance = Base()
    monkeypatch.setattr(base_instance, 'get_dep_chain', lambda: [MockRole('/path/to/role1'), MockRole('/path/to/role2')])
    monkeypatch.setattr(base_instance, 'get_path', lambda: '/path/to/task/file.yml')
    return base_instance

def test_get_search_path_with_dep_chain(mock_base):
    search_path = mock_base.get_search_path()
    assert search_path == ['/path/to/role2', '/path/to/role1', '/path/to/task']

def test_get_search_path_without_dep_chain(monkeypatch):
    base_instance = Base()
    monkeypatch.setattr(base_instance, 'get_dep_chain', lambda: [])
    monkeypatch.setattr(base_instance, 'get_path', lambda: '/path/to/task/file.yml')
    search_path = base_instance.get_search_path()
    assert search_path == ['/path/to/task']

def test_get_search_path_task_dir_in_dep_chain(monkeypatch):
    base_instance = Base()
    monkeypatch.setattr(base_instance, 'get_dep_chain', lambda: [MockRole('/path/to/role1'), MockRole('/path/to/role2')])
    monkeypatch.setattr(base_instance, 'get_path', lambda: '/path/to/role1/file.yml')
    search_path = base_instance.get_search_path()
    assert search_path == ['/path/to/role2', '/path/to/role1']
