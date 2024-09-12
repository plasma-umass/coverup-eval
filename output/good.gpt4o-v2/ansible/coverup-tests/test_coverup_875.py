# file: lib/ansible/plugins/filter/core.py:66-68
# asked: {"lines": [66, 68], "branches": []}
# gained: {"lines": [66, 68], "branches": []}

import pytest
import json
from ansible.parsing.ajson import AnsibleJSONEncoder
from ansible.plugins.filter.core import to_json

def test_to_json():
    # Test data
    data = {"key": "value"}
    
    # Expected JSON string
    expected_json = json.dumps(data, cls=AnsibleJSONEncoder)
    
    # Call the function and assert the result
    result = to_json(data)
    assert result == expected_json

    # Test with additional arguments
    data = {"key": "value"}
    expected_json = json.dumps(data, cls=AnsibleJSONEncoder, indent=4)
    result = to_json(data, indent=4)
    assert result == expected_json

    # Test with keyword arguments
    data = {"key": "value"}
    expected_json = json.dumps(data, cls=AnsibleJSONEncoder, sort_keys=True)
    result = to_json(data, sort_keys=True)
    assert result == expected_json
