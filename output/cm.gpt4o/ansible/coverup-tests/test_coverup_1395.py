# file lib/ansible/parsing/yaml/constructor.py:50-89
# lines [55, 56, 57, 68, 69, 70, 73, 74, 75, 76, 77, 78, 79, 80, 81, 84]
# branches ['54->55', '72->73', '75->76', '75->77', '77->78', '77->84']

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode, ScalarNode
from ansible.parsing.yaml.objects import AnsibleMapping
from unittest import mock

def create_mock_mark():
    mock_mark = mock.Mock()
    mock_mark.line = 1
    mock_mark.column = 1
    return mock_mark

def test_construct_mapping_invalid_node():
    constructor = AnsibleConstructor()
    invalid_node = ScalarNode(tag='tag:yaml.org,2002:str', value='invalid')
    invalid_node.start_mark = create_mock_mark()
    
    with pytest.raises(ConstructorError, match="expected a mapping node, but found"):
        constructor.construct_mapping(invalid_node)

def test_construct_mapping_unhashable_key():
    constructor = AnsibleConstructor()
    key_node = MappingNode(tag='tag:yaml.org,2002:map', value=[])
    key_node.start_mark = create_mock_mark()
    value_node = ScalarNode(tag='tag:yaml.org,2002:str', value='value')
    value_node.start_mark = create_mock_mark()
    node = MappingNode(tag='tag:yaml.org,2002:map', value=[(key_node, value_node)])
    node.start_mark = create_mock_mark()
    
    with pytest.raises(ConstructorError, match="found unacceptable key"):
        constructor.construct_mapping(node)

def test_construct_mapping_duplicate_key_warn(mocker):
    constructor = AnsibleConstructor()
    key_node = ScalarNode(tag='tag:yaml.org,2002:str', value='key')
    key_node.start_mark = create_mock_mark()
    value_node1 = ScalarNode(tag='tag:yaml.org,2002:str', value='value1')
    value_node1.start_mark = create_mock_mark()
    value_node2 = ScalarNode(tag='tag:yaml.org,2002:str', value='value2')
    value_node2.start_mark = create_mock_mark()
    node = MappingNode(tag='tag:yaml.org,2002:map', value=[(key_node, value_node1), (key_node, value_node2)])
    node.start_mark = create_mock_mark()
    
    mocker.patch('ansible.parsing.yaml.constructor.C.DUPLICATE_YAML_DICT_KEY', 'warn')
    mock_warning = mocker.patch('ansible.utils.display.Display.warning')
    
    result = constructor.construct_mapping(node)
    
    assert result['key'] == 'value2'
    mock_warning.assert_called_once_with(mock.ANY)

def test_construct_mapping_duplicate_key_error(mocker):
    constructor = AnsibleConstructor()
    key_node = ScalarNode(tag='tag:yaml.org,2002:str', value='key')
    key_node.start_mark = create_mock_mark()
    value_node1 = ScalarNode(tag='tag:yaml.org,2002:str', value='value1')
    value_node1.start_mark = create_mock_mark()
    value_node2 = ScalarNode(tag='tag:yaml.org,2002:str', value='value2')
    value_node2.start_mark = create_mock_mark()
    node = MappingNode(tag='tag:yaml.org,2002:map', value=[(key_node, value_node1), (key_node, value_node2)])
    node.start_mark = create_mock_mark()
    
    mocker.patch('ansible.parsing.yaml.constructor.C.DUPLICATE_YAML_DICT_KEY', 'error')
    
    with pytest.raises(ConstructorError, match="found a duplicate dict key"):
        constructor.construct_mapping(node)

def test_construct_mapping_duplicate_key_ignore(mocker):
    constructor = AnsibleConstructor()
    key_node = ScalarNode(tag='tag:yaml.org,2002:str', value='key')
    key_node.start_mark = create_mock_mark()
    value_node1 = ScalarNode(tag='tag:yaml.org,2002:str', value='value1')
    value_node1.start_mark = create_mock_mark()
    value_node2 = ScalarNode(tag='tag:yaml.org,2002:str', value='value2')
    value_node2.start_mark = create_mock_mark()
    node = MappingNode(tag='tag:yaml.org,2002:map', value=[(key_node, value_node1), (key_node, value_node2)])
    node.start_mark = create_mock_mark()
    
    mocker.patch('ansible.parsing.yaml.constructor.C.DUPLICATE_YAML_DICT_KEY', 'ignore')
    mock_debug = mocker.patch('ansible.utils.display.Display.debug')
    
    result = constructor.construct_mapping(node)
    
    assert result['key'] == 'value2'
    mock_debug.assert_called_once_with(mock.ANY)
