# file lib/ansible/plugins/filter/core.py:66-68
# lines [66, 68]
# branches []

import pytest
import json
from ansible.plugins.filter.core import to_json
from ansible.parsing.ajson import AnsibleJSONEncoder

def test_to_json(mocker):
    # Mocking json.dumps to ensure it is called with AnsibleJSONEncoder
    mock_dumps = mocker.patch('json.dumps', wraps=json.dumps)
    
    # Test data
    data = {"key": "value"}
    
    # Call the function
    result = to_json(data)
    
    # Assertions
    mock_dumps.assert_called_once_with(data, cls=AnsibleJSONEncoder)
    assert result == json.dumps(data, cls=AnsibleJSONEncoder)
    
    # Clean up
    mocker.stopall()
