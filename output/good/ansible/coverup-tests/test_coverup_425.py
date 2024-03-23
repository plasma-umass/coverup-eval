# file lib/ansible/parsing/yaml/constructor.py:123-133
# lines [123, 124, 125, 126, 127, 128, 129, 131, 133]
# branches ['126->127', '126->131']

import pytest
from yaml.nodes import ScalarNode
from ansible.parsing.yaml.constructor import AnsibleConstructor

# Mock wrap_var function to be used within the test
def mock_wrap_var(value):
    return value

# Test function to cover construct_yaml_unsafe method
def test_construct_yaml_unsafe(mocker):
    # Mock the wrap_var function in the module
    wrap_var_mock = mocker.patch('ansible.parsing.yaml.constructor.wrap_var', side_effect=mock_wrap_var)

    # Create an instance of AnsibleConstructor
    constructor = AnsibleConstructor()

    # Create a ScalarNode with tag 'tag:yaml.org,2002:str' which corresponds to a string
    node = ScalarNode(tag='tag:yaml.org,2002:str', value='test string')

    # Call the construct_yaml_unsafe method with the node
    result = constructor.construct_yaml_unsafe(node)

    # Assert that the result is the string 'test string'
    assert result == 'test string'

    # Create a ScalarNode with an unsupported tag to trigger the AttributeError
    node_unsupported = ScalarNode(tag='tag:yaml.org,2002:unsupported', value='test')

    # Call the construct_yaml_unsafe method with the unsupported node
    result_unsupported = constructor.construct_yaml_unsafe(node_unsupported)

    # Assert that the result is the original value 'test'
    assert result_unsupported == 'test'

    # Verify that wrap_var was called twice
    assert wrap_var_mock.call_count == 2
