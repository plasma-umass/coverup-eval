# file thefuck/shells/generic.py:73-74
# lines [73, 74]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_and_method():
    shell = Generic()
    
    # Test with no commands
    result = shell.and_()
    assert result == '', "Expected empty string when no commands are passed"
    
    # Test with one command
    result = shell.and_('ls')
    assert result == 'ls', "Expected 'ls' when one command is passed"
    
    # Test with multiple commands
    result = shell.and_('ls', 'pwd', 'echo "Hello"')
    assert result == 'ls && pwd && echo "Hello"', "Expected 'ls && pwd && echo \"Hello\"' when multiple commands are passed"
