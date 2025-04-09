# file: lib/ansible/parsing/yaml/constructor.py:91-99
# asked: {"lines": [91, 94, 95, 97, 99], "branches": []}
# gained: {"lines": [91, 94, 95, 97, 99], "branches": []}

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.yaml.objects import AnsibleUnicode
from yaml.nodes import ScalarNode

@pytest.fixture
def constructor():
    return AnsibleConstructor()

def test_construct_yaml_str(constructor, mocker):
    # Mock the node and its value
    node = ScalarNode(tag='tag:yaml.org,2002:str', value='test_value')
    
    # Mock the _node_position_info method to return a valid tuple
    mocker.patch.object(constructor, '_node_position_info', return_value=('mocked_source', 1, 1))
    
    # Call the method
    result = constructor.construct_yaml_str(node)
    
    # Assertions to verify the postconditions
    assert isinstance(result, AnsibleUnicode)
    assert result == 'test_value'
    assert result.ansible_pos == ('mocked_source', 1, 1)
