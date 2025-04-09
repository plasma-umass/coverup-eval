# file lib/ansible/parsing/quoting.py:27-31
# lines [27, 29, 30, 31]
# branches ['29->30', '29->31']

import pytest
from ansible.parsing.quoting import is_quoted, unquote

def test_unquote(mocker):
    # Mocking is_quoted to control its behavior
    mocker.patch('ansible.parsing.quoting.is_quoted', return_value=True)
    
    # Test case where the string is quoted
    quoted_string = '"hello"'
    result = unquote(quoted_string)
    assert result == 'hello', f"Expected 'hello', but got {result}"
    
    # Test case where the string is not quoted
    mocker.patch('ansible.parsing.quoting.is_quoted', return_value=False)
    unquoted_string = 'world'
    result = unquote(unquoted_string)
    assert result == 'world', f"Expected 'world', but got {result}"
