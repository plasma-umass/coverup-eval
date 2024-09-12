# file: lib/ansible/parsing/yaml/constructor.py:123-133
# asked: {"lines": [124, 125, 126, 127, 128, 129, 131, 133], "branches": [[126, 127], [126, 131]]}
# gained: {"lines": [124, 125, 126, 127, 128, 129, 131, 133], "branches": [[126, 127]]}

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.yaml.constructor import AnsibleConstructor
from yaml.nodes import Node

@pytest.fixture
def mock_node():
    node = Mock(spec=Node)
    return node

@pytest.fixture
def constructor():
    return AnsibleConstructor()

def test_construct_yaml_unsafe_with_id(mock_node, constructor):
    mock_node.id = 'yaml_map'
    with patch.object(constructor, 'construct_yaml_map', return_value='mapped_value') as mock_construct:
        result = constructor.construct_yaml_unsafe(mock_node)
        mock_construct.assert_called_once_with(mock_node)
        assert result == 'mapped_value'

def test_construct_yaml_unsafe_without_id(mock_node, constructor):
    del mock_node.id
    with patch.object(constructor, 'construct_object', return_value='default_value') as mock_construct:
        result = constructor.construct_yaml_unsafe(mock_node)
        mock_construct.assert_called_once_with(mock_node)
        assert result == 'default_value'

def test_construct_yaml_unsafe_with_invalid_id(mock_node, constructor):
    mock_node.id = 'invalid_id'
    with patch.object(constructor, 'construct_object', return_value='default_value') as mock_construct:
        result = constructor.construct_yaml_unsafe(mock_node)
        mock_construct.assert_called_once_with(mock_node)
        assert result == 'default_value'
