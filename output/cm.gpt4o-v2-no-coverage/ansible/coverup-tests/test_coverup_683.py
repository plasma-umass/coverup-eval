# file: lib/ansible/parsing/yaml/constructor.py:43-48
# asked: {"lines": [43, 44, 45, 46, 47, 48], "branches": []}
# gained: {"lines": [43, 44, 45, 46, 47, 48], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleMapping
from yaml.nodes import MappingNode

@pytest.fixture
def mock_node():
    return MagicMock(spec=MappingNode)

@pytest.fixture
def constructor():
    return AnsibleConstructor()

def test_construct_yaml_map(constructor, mock_node):
    # Mock the methods called within construct_yaml_map
    mock_node_position_info = MagicMock(return_value=("mock_source", 1, 1))
    constructor._node_position_info = mock_node_position_info
    mock_construct_mapping = MagicMock(return_value={"key": "value"})
    constructor.construct_mapping = mock_construct_mapping

    # Create the generator
    generator = constructor.construct_yaml_map(mock_node)
    
    # Get the yielded value
    data = next(generator)
    
    # Ensure the yielded value is an instance of AnsibleMapping
    assert isinstance(data, AnsibleMapping)
    
    # Continue execution to complete the generator
    try:
        next(generator)
    except StopIteration:
        pass
    
    # Verify that data has been updated correctly
    assert data == {"key": "value"}
    assert data.ansible_pos == ("mock_source", 1, 1)
    
    # Verify that the mocked methods were called correctly
    mock_node_position_info.assert_called_once_with(mock_node)
    mock_construct_mapping.assert_called_once_with(mock_node)
