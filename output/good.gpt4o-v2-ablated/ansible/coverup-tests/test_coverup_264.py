# file: lib/ansible/parsing/yaml/constructor.py:135-147
# asked: {"lines": [135, 138, 139, 145, 147], "branches": []}
# gained: {"lines": [135, 138, 139, 145, 147], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.parsing.yaml.constructor import AnsibleConstructor

@pytest.fixture
def mock_node():
    mock = Mock()
    mock.start_mark.line = 10
    mock.start_mark.column = 5
    mock.start_mark.name = 'mock_file.yaml'
    return mock

@pytest.fixture
def constructor():
    constructor = AnsibleConstructor()
    constructor._ansible_file_name = None
    return constructor

def test_node_position_info_with_default_datasource(constructor, mock_node):
    datasource, line, column = constructor._node_position_info(mock_node)
    assert datasource == 'mock_file.yaml'
    assert line == 11
    assert column == 6

def test_node_position_info_with_custom_datasource(constructor, mock_node):
    constructor._ansible_file_name = 'custom_file.yaml'
    datasource, line, column = constructor._node_position_info(mock_node)
    assert datasource == 'custom_file.yaml'
    assert line == 11
    assert column == 6
