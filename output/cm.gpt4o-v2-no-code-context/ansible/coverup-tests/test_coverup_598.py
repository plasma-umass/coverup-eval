# file: lib/ansible/parsing/yaml/constructor.py:117-121
# asked: {"lines": [117, 118, 119, 120, 121], "branches": []}
# gained: {"lines": [117, 118, 119, 120, 121], "branches": []}

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleSequence
from yaml.nodes import SequenceNode
from unittest.mock import MagicMock

@pytest.fixture
def constructor():
    return AnsibleConstructor()

def test_construct_yaml_seq(constructor, mocker):
    # Mocking the node and its position info
    node = SequenceNode(tag='tag:yaml.org,2002:seq', value=[])
    mocker.patch.object(constructor, 'construct_sequence', return_value=[1, 2, 3])
    mocker.patch.object(constructor, '_node_position_info', return_value=('source', 1, 2))

    # Using the generator
    generator = constructor.construct_yaml_seq(node)
    data = next(generator)
    
    # Assertions to verify the state
    assert isinstance(data, AnsibleSequence)
    assert data == []
    
    # Complete the generator
    try:
        next(generator)
    except StopIteration:
        pass
    
    # Assertions to verify the final state
    assert data == [1, 2, 3]
    assert data.ansible_pos == ('source', 1, 2)
