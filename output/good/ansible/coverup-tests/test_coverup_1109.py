# file lib/ansible/parsing/yaml/dumper.py:49-50
# lines [49, 50]
# branches []

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml

# Test function to cover represent_unicode method
def test_represent_unicode():
    # Setup
    test_string = u"test_unicode_string"
    dumper = AnsibleDumper(None)

    # Exercise
    actual_representation = dumper.represent_data(test_string)

    # Verify
    assert isinstance(actual_representation, yaml.nodes.ScalarNode)
    assert actual_representation.value == test_string

    # Cleanup - nothing to clean up as no external resources or state changes were made
