# file lib/ansible/parsing/yaml/dumper.py:53-54
# lines [53, 54]
# branches []

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml
import base64

# Test function to cover represent_binary method
def test_represent_binary():
    # Create an instance of AnsibleDumper
    dumper = AnsibleDumper(None)

    # Binary data to be represented
    binary_data = b"binary\x00data"

    # Call the represent_binary method
    node = dumper.represent_binary(binary_data)

    # Assertions to check if the method is covered and returns the correct result
    assert isinstance(node, yaml.nodes.ScalarNode), "Should return a ScalarNode"
    assert node.tag == u'tag:yaml.org,2002:binary', "Should have the correct tag for binary data"
    # The value should be base64 encoded, so we decode it to compare
    assert base64.b64decode(node.value.encode('utf-8')) == binary_data, "Should correctly represent the binary data"
