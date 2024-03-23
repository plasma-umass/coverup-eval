# file lib/ansible/plugins/filter/core.py:66-68
# lines [66, 68]
# branches []

import json
import pytest
from ansible.plugins.filter.core import to_json
from ansible.parsing.ajson import AnsibleJSONEncoder

# Assuming the AnsibleJSONEncoder is already properly tested, we just need to test the to_json function.

def test_to_json():
    # Test with a simple data structure
    data = {"key": "value"}
    expected_json = json.dumps(data, cls=AnsibleJSONEncoder)
    assert to_json(data) == expected_json

    # Test with a more complex data structure including types that AnsibleJSONEncoder should handle
    data_complex = {
        "key": "value",
        "list": [1, 2, 3],
        "dict": {"nested_key": "nested_value"}
    }
    expected_json_complex = json.dumps(data_complex, cls=AnsibleJSONEncoder)
    assert to_json(data_complex) == expected_json_complex

    # Test with additional args and kwargs
    data_with_indent = {"key": "value"}
    expected_json_with_indent = json.dumps(data_with_indent, cls=AnsibleJSONEncoder, indent=4)
    assert to_json(data_with_indent, indent=4) == expected_json_with_indent

# Note: No cleanup is necessary for this test as it does not modify any external state or configuration.
