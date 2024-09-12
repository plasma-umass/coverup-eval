# file: lib/ansible/module_utils/splitter.py:215-219
# asked: {"lines": [215, 217, 218, 219], "branches": [[217, 218], [217, 219]]}
# gained: {"lines": [215, 217, 218, 219], "branches": [[217, 218], [217, 219]]}

import pytest
from ansible.module_utils.splitter import unquote

def is_quoted(data):
    ''' Helper function to determine if a string is quoted '''
    return (data.startswith('"') and data.endswith('"')) or (data.startswith("'") and data.endswith("'"))

@pytest.mark.parametrize("input_str, expected_output", [
    ('"quoted"', 'quoted'),
    ("'quoted'", 'quoted'),
    ('"mismatched\'', '"mismatched\''),
    ('noquotes', 'noquotes'),
    ('"nested\'quotes\'"', 'nested\'quotes\''),
    ("'nested\"quotes\"'", 'nested"quotes"'),
])
def test_unquote(input_str, expected_output):
    assert unquote(input_str) == expected_output
