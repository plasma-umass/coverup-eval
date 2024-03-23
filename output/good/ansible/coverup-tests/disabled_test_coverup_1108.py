# file lib/ansible/parsing/yaml/dumper.py:33-37
# lines [33, 34]
# branches []

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml

# Define a custom object to test the AnsibleDumper
class CustomObject:
    pass

# Define a representer for the custom object
def custom_object_representer(dumper, data):
    return dumper.represent_scalar('!CustomObject', 'This is a custom object')

# Add the representer to the AnsibleDumper
AnsibleDumper.add_representer(CustomObject, custom_object_representer)

# Test function to check if the representer is correctly added and used
def test_ansible_dumper_with_custom_object():
    # Create an instance of the custom object
    obj = CustomObject()

    # Dump the custom object using the AnsibleDumper
    dumped_data = yaml.dump(obj, Dumper=AnsibleDumper)

    # Check if the dumped data contains the correct representation
    assert '!CustomObject This is a custom object\n' in dumped_data

# Clean up after the test by removing the added representer
def teardown_function(function):
    AnsibleDumper.yaml_representers.pop(CustomObject, None)
