# file: lib/ansible/parsing/yaml/constructor.py:50-89
# asked: {"lines": [50, 54, 55, 56, 57, 58, 59, 62, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 84, 86, 87, 89], "branches": [[54, 55], [54, 58], [64, 65], [64, 89], [72, 73], [72, 86], [75, 76], [75, 77], [77, 78], [77, 84]]}
# gained: {"lines": [50, 54, 55, 56, 57, 58, 59, 62, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 84, 86, 87, 89], "branches": [[54, 55], [54, 58], [64, 65], [64, 89], [72, 73], [72, 86], [75, 76], [75, 77], [77, 78], [77, 84]]}

import pytest
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode, ScalarNode, Node
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleMapping
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_node():
    node = MagicMock(spec=MappingNode)
    node.start_mark = MagicMock()
    node.start_mark.line = 1
    node.start_mark.column = 1
    node.start_mark.name = 'testfile'
    node.id = 'mapping'
    node.value = [(ScalarNode(tag='tag:yaml.org,2002:str', value='key1'), ScalarNode(tag='tag:yaml.org,2002:str', value='value1')),
                  (ScalarNode(tag='tag:yaml.org,2002:str', value='key2'), ScalarNode(tag='tag:yaml.org,2002:str', value='value2'))]
    return node

@pytest.fixture
def constructor():
    return AnsibleConstructor()

def test_construct_mapping_valid(mock_node, constructor):
    with patch.object(constructor, 'construct_object', side_effect=lambda x, deep: x.value):
        with patch.object(constructor, 'flatten_mapping'):
            result = constructor.construct_mapping(mock_node)
            assert isinstance(result, AnsibleMapping)
            assert result['key1'] == 'value1'
            assert result['key2'] == 'value2'
            assert result.ansible_pos == ('testfile', 2, 2)

def test_construct_mapping_invalid_node(constructor):
    invalid_node = MagicMock(spec=Node)
    invalid_node.id = 'scalar'
    invalid_node.start_mark = MagicMock()
    with pytest.raises(ConstructorError, match="expected a mapping node, but found scalar"):
        constructor.construct_mapping(invalid_node)

def test_construct_mapping_unhashable_key(mock_node, constructor):
    mock_node.value = [(ScalarNode(tag='tag:yaml.org,2002:seq', value='[1, 2, 3]'), ScalarNode(tag='tag:yaml.org,2002:str', value='value1'))]
    with patch.object(constructor, 'construct_object', side_effect=lambda x, deep: [1, 2, 3]):
        with patch.object(constructor, 'flatten_mapping'):
            with pytest.raises(ConstructorError, match="found unacceptable key"):
                constructor.construct_mapping(mock_node)

def test_construct_mapping_duplicate_key(mock_node, constructor):
    mock_node.value.append((ScalarNode(tag='tag:yaml.org,2002:str', value='key1'), ScalarNode(tag='tag:yaml.org,2002:str', value='value3')))
    with patch.object(constructor, 'construct_object', side_effect=lambda x, deep: x.value):
        with patch.object(constructor, 'flatten_mapping'):
            with patch('ansible.parsing.yaml.constructor.C.DUPLICATE_YAML_DICT_KEY', 'error'):
                with pytest.raises(ConstructorError, match="found a duplicate dict key"):
                    constructor.construct_mapping(mock_node)
            with patch('ansible.parsing.yaml.constructor.C.DUPLICATE_YAML_DICT_KEY', 'warn'):
                with patch('ansible.parsing.yaml.constructor.display.warning') as mock_warning:
                    constructor.construct_mapping(mock_node)
                    mock_warning.assert_called_once()
            with patch('ansible.parsing.yaml.constructor.C.DUPLICATE_YAML_DICT_KEY', 'ignore'):
                with patch('ansible.parsing.yaml.constructor.display.debug') as mock_debug:
                    constructor.construct_mapping(mock_node)
                    mock_debug.assert_called_once()
