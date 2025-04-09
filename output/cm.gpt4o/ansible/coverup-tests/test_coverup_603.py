# file lib/ansible/parsing/yaml/constructor.py:43-48
# lines [43, 44, 45, 46, 47, 48]
# branches []

import pytest
from unittest.mock import patch
from ansible.parsing.yaml.constructor import AnsibleConstructor, AnsibleMapping
from yaml.nodes import MappingNode

@pytest.fixture
def mock_node():
    return MappingNode(tag='tag:yaml.org,2002:map', value=[])

def test_construct_yaml_map(mock_node):
    constructor = AnsibleConstructor()
    
    with patch.object(AnsibleConstructor, 'construct_mapping', return_value={'key': 'value'}) as mock_construct_mapping, \
         patch.object(AnsibleConstructor, '_node_position_info', return_value=('source', 1, 1)) as mock_node_position_info:
        
        generator = constructor.construct_yaml_map(mock_node)
        data = next(generator)
        
        assert isinstance(data, AnsibleMapping)
        
        # Complete the generator
        try:
            next(generator)
        except StopIteration:
            pass
        
        assert data == {'key': 'value'}
        assert data.ansible_pos == ('source', 1, 1)
        mock_construct_mapping.assert_called_once_with(mock_node)
        mock_node_position_info.assert_called_once_with(mock_node)
