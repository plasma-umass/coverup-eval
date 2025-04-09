# file: lib/ansible/parsing/yaml/constructor.py:43-48
# asked: {"lines": [43, 44, 45, 46, 47, 48], "branches": []}
# gained: {"lines": [43, 44, 45, 46, 47, 48], "branches": []}

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleMapping
from yaml.nodes import MappingNode, ScalarNode

@pytest.fixture
def mock_node():
    key_node = ScalarNode(tag='tag:yaml.org,2002:str', value='key')
    value_node = ScalarNode(tag='tag:yaml.org,2002:str', value='value')
    return MappingNode(tag='tag:yaml.org,2002:map', value=[(key_node, value_node)])

def test_construct_yaml_map(mock_node, mocker):
    constructor = AnsibleConstructor()
    mocker.patch.object(constructor, 'construct_mapping', return_value={'key': 'value'})
    mocker.patch.object(constructor, '_node_position_info', return_value=('source', 1, 1))

    generator = constructor.construct_yaml_map(mock_node)
    data = next(generator)
    
    assert isinstance(data, AnsibleMapping)
    assert not data  # Initially empty

    # Complete the generator
    try:
        next(generator)
    except StopIteration:
        pass

    assert data == {'key': 'value'}
    assert data.ansible_pos == ('source', 1, 1)
