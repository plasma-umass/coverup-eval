# file thefuck/shells/generic.py:49-50
# lines [49, 50]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_history_line():
    generic_shell = Generic()
    command_script = "echo 'Hello, World!'"
    
    # Call the method and check the return value
    result = generic_shell._get_history_line(command_script)
    
    # Assert that the result is an empty string
    assert result == ''
