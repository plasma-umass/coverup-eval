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
    constructor.construct_sequence = MagicMock(return_value=[1, 2, 3])
    constructor._node_position_info = MagicMock(return_value=('source', 1, 2))

    # Create a generator from the method
    generator = constructor.construct_yaml_seq(mock_node)
    
    # Get the first yielded value
    data = next(generator)
    
    # Ensure the data is an instance of AnsibleSequence
    assert isinstance(data, AnsibleSequence)
    
    # Ensure the data is initially empty
    assert len(data) == 0
    
    # Continue execution to complete the method
    try:
        next(generator)
    except StopIteration:
        pass
    
    # Ensure the data has been extended with the sequence
    assert data == [1, 2, 3]
    
    # Ensure the ansible_pos attribute is set correctly
    assert data.ansible_pos == ('source', 1, 2)
