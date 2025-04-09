# file: lib/ansible/parsing/yaml/constructor.py:135-147
# asked: {"lines": [135, 138, 139, 145, 147], "branches": []}
# gained: {"lines": [135, 138, 139, 145, 147], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.parsing.yaml.constructor import AnsibleConstructor

@pytest.fixture
def mock_node():
    mock = Mock()
    mock.start_mark.column = 5
    mock.start_mark.line = 10
    mock.start_mark.name = 'mock_file.yaml'
    return mock

def test_node_position_info_with_filename(mock_node):
    constructor = AnsibleConstructor(file_name='test_file.yaml')
    datasource, line, column = constructor._node_position_info(mock_node)
    
    assert datasource == 'test_file.yaml'
    assert line == 11
    assert column == 6

def test_node_position_info_without_filename(mock_node):
    constructor = AnsibleConstructor()
    datasource, line, column = constructor._node_position_info(mock_node)
    
    assert datasource == 'mock_file.yaml'
    assert line == 11
    assert column == 6
