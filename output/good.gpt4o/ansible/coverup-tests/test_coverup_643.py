# file lib/ansible/parsing/yaml/constructor.py:135-147
# lines [135, 138, 139, 145, 147]
# branches []

import pytest
from unittest.mock import Mock
from ansible.parsing.yaml.constructor import AnsibleConstructor
from yaml.nodes import Node
from yaml import Mark

@pytest.fixture
def mock_node():
    start_mark = Mark(name='test_file.yml', index=0, line=10, column=5, buffer=None, pointer=None)
    end_mark = Mark(name='test_file.yml', index=0, line=10, column=5, buffer=None, pointer=None)
    return Node(tag='tag:yaml.org,2002:map', value=[], start_mark=start_mark, end_mark=end_mark)

def test_node_position_info(mock_node, mocker):
    constructor = AnsibleConstructor()
    mocker.patch.object(constructor, '_ansible_file_name', 'mock_file.yml')
    
    datasource, line, column = constructor._node_position_info(mock_node)
    
    assert datasource == 'mock_file.yml'
    assert line == 11  # 10 + 1
    assert column == 6  # 5 + 1

def test_node_position_info_no_ansible_file_name(mock_node):
    constructor = AnsibleConstructor()
    constructor._ansible_file_name = None
    
    datasource, line, column = constructor._node_position_info(mock_node)
    
    assert datasource == 'test_file.yml'
    assert line == 11  # 10 + 1
    assert column == 6  # 5 + 1
