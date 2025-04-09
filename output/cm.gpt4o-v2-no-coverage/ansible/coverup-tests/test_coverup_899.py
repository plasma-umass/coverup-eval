# file: lib/ansible/plugins/filter/core.py:71-73
# asked: {"lines": [71, 73], "branches": []}
# gained: {"lines": [71, 73], "branches": []}

import pytest
from ansible.plugins.filter.core import to_nice_json
from ansible.parsing.ajson import AnsibleJSONEncoder
import json

def test_to_nice_json():
    data = {'key': 'value'}
    expected_json = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), cls=AnsibleJSONEncoder)
    
    result = to_nice_json(data)
    
    assert result == expected_json

    # Test with additional arguments
    result_with_args = to_nice_json(data, indent=2, sort_keys=False)
    expected_json_with_args = json.dumps(data, indent=2, sort_keys=False, separators=(',', ': '), cls=AnsibleJSONEncoder)
    
    assert result_with_args == expected_json_with_args
