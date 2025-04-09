# file lib/ansible/plugins/inventory/toml.py:128-149
# lines [142, 143, 144, 145, 146, 147, 149]
# branches ['142->143', '142->144', '144->145', '144->146', '146->147', '146->149']

import pytest
from ansible.parsing.yaml.objects import AnsibleUnicode
from ansible.plugins.inventory.toml import convert_yaml_objects_to_native

def test_convert_yaml_objects_to_native_with_text_type(mocker):
    # Mock the text_type to be AnsibleUnicode to simulate the condition
    mocker.patch('ansible.plugins.inventory.toml.text_type', new=AnsibleUnicode)

    # Create a test object with AnsibleUnicode type
    test_obj = {
        'key1': AnsibleUnicode('value1'),
        'key2': [AnsibleUnicode('value2'), AnsibleUnicode('value3')],
        'key3': {
            'nested_key': AnsibleUnicode('nested_value')
        }
    }

    # Call the function to test
    result = convert_yaml_objects_to_native(test_obj)

    # Assertions to check if the conversion happened correctly
    assert isinstance(result, dict), "Result should be a dictionary"
    assert isinstance(result['key1'], str), "Values should be converted to native str"
    assert isinstance(result['key2'][0], str), "List items should be converted to native str"
    assert isinstance(result['key3']['nested_key'], str), "Nested values should be converted to native str"

    # Clean up the mock
    mocker.stopall()
