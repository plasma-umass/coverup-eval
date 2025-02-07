# file: lib/ansible/playbook/base.py:878-895
# asked: {"lines": [878, 883, 885, 887, 888, 891, 892, 893, 895], "branches": [[887, 888], [887, 891], [892, 893], [892, 895]]}
# gained: {"lines": [878, 883, 885, 887, 888, 891, 892, 893, 895], "branches": [[887, 888], [887, 891], [892, 893]]}

import pytest
import os
from unittest.mock import MagicMock
from ansible.playbook.base import Base

@pytest.fixture
def base_instance():
    base = Base()
    base._ds = MagicMock()
    base._ds._data_source = "/path/to/datasource"
    base._ds._line_number = 42
    return base

def test_get_search_path_with_dep_chain(base_instance, mocker):
    # Mocking get_dep_chain to return a list of objects with _role_path attribute
    dep_chain_mock = [MagicMock(_role_path="/path/to/role1"), MagicMock(_role_path="/path/to/role2")]
    mocker.patch.object(base_instance, 'get_dep_chain', return_value=dep_chain_mock)
    
    # Mocking get_path to return a specific path
    mocker.patch.object(base_instance, 'get_path', return_value="/path/to/taskfile/taskfile.yml")
    
    search_path = base_instance.get_search_path()
    
    assert search_path == ["/path/to/role2", "/path/to/role1", "/path/to/taskfile"]

def test_get_search_path_without_dep_chain(base_instance, mocker):
    # Mocking get_dep_chain to return None
    mocker.patch.object(base_instance, 'get_dep_chain', return_value=None)
    
    # Mocking get_path to return a specific path
    mocker.patch.object(base_instance, 'get_path', return_value="/path/to/taskfile/taskfile.yml")
    
    search_path = base_instance.get_search_path()
    
    assert search_path == ["/path/to/taskfile"]
