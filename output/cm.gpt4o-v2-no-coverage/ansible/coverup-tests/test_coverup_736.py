# file: lib/ansible/parsing/yaml/constructor.py:117-121
# asked: {"lines": [117, 118, 119, 120, 121], "branches": []}
# gained: {"lines": [117, 118, 119, 120, 121], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleSequence
from yaml.nodes import SequenceNode

@pytest.fixture
def mock_node():
    return MagicMock(spec=SequenceNode)

@pytest.fixture
def constructor():
    return AnsibleConstructor()

def test_construct_yaml_seq(constructor, mock_node):
    # Mock the methods used within construct_yaml_seq
    mock_construct_sequence = MagicMock(return_value=[1, 2, 3])
    mock_node_position_info = MagicMock(return_value=('source', 1, 2))
    
    constructor.construct_sequence = mock_construct_sequence
    constructor._node_position_info = mock_node_position_info
    
    # Call the method and get the generator
    generator = constructor.construct_yaml_seq(mock_node)
    
    # Get the first yielded value
    data = next(generator)
    
    # Ensure the yielded value is an instance of AnsibleSequence
    assert isinstance(data, AnsibleSequence)
    
    # Continue execution to complete the generator
    try:
        next(generator)
    except StopIteration:
        pass
    
    # Verify that data has been extended and ansible_pos has been set
    assert data == [1, 2, 3]
    assert data.ansible_pos == ('source', 1, 2)
    
    # Verify that the mocked methods were called with the correct arguments
    mock_construct_sequence.assert_called_once_with(mock_node)
    mock_node_position_info.assert_called_once_with(mock_node)
