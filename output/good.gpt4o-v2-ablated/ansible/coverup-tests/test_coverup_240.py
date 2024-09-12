# file: lib/ansible/parsing/quoting.py:27-31
# asked: {"lines": [27, 29, 30, 31], "branches": [[29, 30], [29, 31]]}
# gained: {"lines": [27, 29, 30, 31], "branches": [[29, 30], [29, 31]]}

import pytest
from ansible.parsing.quoting import unquote

def is_quoted(data):
    ''' Helper function to determine if a string is quoted '''
    if len(data) < 2:
        return False
    return (data[0] == data[-1]) and data[0] in ('"', "'")

@pytest.mark.parametrize("input_str, expected_output", [
    ('"hello"', 'hello'),
    ("'world'", 'world'),
    ('"hello', '"hello'),
    ("world'", "world'"),
    ('noquotes', 'noquotes'),
    ('""', ''),
    ("''", ''),
    ('"a"', 'a'),
    ("'b'", 'b'),
])
def test_unquote(input_str, expected_output):
    assert unquote(input_str) == expected_output
