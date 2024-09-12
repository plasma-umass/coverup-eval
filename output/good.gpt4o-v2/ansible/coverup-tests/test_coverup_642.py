# file: lib/ansible/parsing/yaml/constructor.py:43-48
# asked: {"lines": [43, 44, 45, 46, 47, 48], "branches": []}
# gained: {"lines": [43, 44, 45, 46, 47, 48], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleMapping
from yaml.nodes import MappingNode

@pytest.fixture
def mock_constructor():
    constructor = AnsibleConstructor()
    constructor.construct_mapping = MagicMock(return_value={'key': 'value'})
    constructor._node_position_info = MagicMock(return_value=('source', 1, 2))
    return constructor

def test_construct_yaml_map(mock_constructor):
    node = MappingNode(tag='tag:yaml.org,2002:map', value=[])
    generator = mock_constructor.construct_yaml_map(node)
    data = next(generator)
    
    assert isinstance(data, AnsibleMapping)
    
    # Complete the generator
    try:
        next(generator)
    except StopIteration:
        pass
    
    assert data == {'key': 'value'}
    assert data.ansible_pos == ('source', 1, 2)
    mock_constructor.construct_mapping.assert_called_once_with(node)
    mock_constructor._node_position_info.assert_called_once_with(node)
