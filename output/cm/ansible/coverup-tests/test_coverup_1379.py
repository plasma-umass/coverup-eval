# file lib/ansible/parsing/yaml/constructor.py:123-133
# lines [128, 129]
# branches ['126->131']

import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from yaml.nodes import ScalarNode

@pytest.fixture
def ansible_constructor():
    return AnsibleConstructor()

@pytest.fixture
def cleanup(mocker):
    # Use mocker to ensure that any state changes during the test are reverted after the test
    mocker.patch.object(AnsibleConstructor, 'construct_object', side_effect=AnsibleConstructor.construct_object)

def test_construct_yaml_unsafe_with_nonexistent_constructor(ansible_constructor, cleanup, mocker):
    # Create a ScalarNode with a non-existent constructor method
    node = ScalarNode(tag='!nonexistent', value='test_value')
    # Set the id attribute to a non-existent constructor
    setattr(node, 'id', 'nonexistent')
    
    # Mock the construct_object to avoid side effects
    mock_construct_object = mocker.patch.object(ansible_constructor, 'construct_object', return_value='mocked_value')
    
    # Call the method that should trigger the AttributeError
    result = ansible_constructor.construct_yaml_unsafe(node)
    
    # Assert that the mock_construct_object was called
    mock_construct_object.assert_called_once_with(node)
    
    # Assert that the result is the mocked value
    assert result == 'mocked_value', "The construct_yaml_unsafe method did not fall back to construct_object on AttributeError"
