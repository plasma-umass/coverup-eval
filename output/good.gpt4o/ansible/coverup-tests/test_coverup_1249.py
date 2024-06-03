# file lib/ansible/parsing/yaml/constructor.py:123-133
# lines [128, 129]
# branches ['126->131']

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.yaml.constructor import AnsibleConstructor
from yaml.nodes import Node

@pytest.fixture
def mock_node():
    node = Mock(spec=Node)
    node.id = 'nonexistent_constructor'
    return node

def test_construct_yaml_unsafe_attribute_error(mock_node):
    constructor = AnsibleConstructor()
    
    with patch.object(constructor, 'construct_object', return_value='mocked_value'):
        result = constructor.construct_yaml_unsafe(mock_node)
        
        assert result == 'mocked_value'

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
