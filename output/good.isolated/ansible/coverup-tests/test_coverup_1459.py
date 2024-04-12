# file lib/ansible/parsing/splitter.py:42-46
# lines [44]
# branches []

import pytest
from ansible.parsing.splitter import _decode_escapes

def test_decode_escapes_executes_line_44():
    # Test string containing unicode escape sequences
    test_string = '\\u2603\\U0001F600\\x41\\n'
    expected_string = '☃😀A\n'

    # Call the function that uses the _decode_escapes
    result_string = _decode_escapes(test_string)

    # Assert that the result matches the expected string
    assert result_string == expected_string
