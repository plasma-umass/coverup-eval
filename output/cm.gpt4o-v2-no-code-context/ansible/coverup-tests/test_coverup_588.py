# file: lib/ansible/parsing/yaml/constructor.py:135-147
# asked: {"lines": [135, 138, 139, 145, 147], "branches": []}
# gained: {"lines": [135, 138, 139, 145, 147], "branches": []}

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from yaml.nodes import ScalarNode, SequenceNode, MappingNode
from unittest.mock import Mock

@pytest.fixture
def constructor():
    return AnsibleConstructor()

def test_node_position_info_with_filename(constructor):
    mock_node = Mock()
    mock_node.start_mark.column = 5
    mock_node.start_mark.line = 10
    mock_node.start_mark.name = 'mock_file.yaml'
    
    constructor._ansible_file_name = 'test_file.yaml'
    
    datasource, line, column = constructor._node_position_info(mock_node)
    
    assert datasource == 'test_file.yaml'
    assert line == 11
    assert column == 6

def test_node_position_info_without_filename(constructor):
    mock_node = Mock()
    mock_node.start_mark.column = 5
    mock_node.start_mark.line = 10
    mock_node.start_mark.name = 'mock_file.yaml'
    
    constructor._ansible_file_name = None
    
    datasource, line, column = constructor._node_position_info(mock_node)
    
    assert datasource == 'mock_file.yaml'
    assert line == 11
    assert column == 6
