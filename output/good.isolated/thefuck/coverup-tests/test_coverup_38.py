# file thefuck/types.py:48-52
# lines [48, 49, 50, 52]
# branches ['49->50', '49->52']

import pytest
from thefuck.types import Command

def test_command_eq():
    # Setup two Command instances with the same script and output
    command1 = Command(script='ls -la', output='total 0')
    command2 = Command(script='ls -la', output='total 0')
    
    # Test equality of two Command instances
    assert command1 == command2, "Command instances with the same script and output should be equal"
    
    # Test inequality of Command instance with other types
    assert not (command1 == 'ls -la'), "Command instance should not be equal to a string"
    
    # Test inequality of Command instances with different script or output
    command3 = Command(script='ls -la', output='total 1')
    assert not (command1 == command3), "Command instances with different output should not be equal"
    
    command4 = Command(script='ls -l', output='total 0')
    assert not (command1 == command4), "Command instances with different script should not be equal"
