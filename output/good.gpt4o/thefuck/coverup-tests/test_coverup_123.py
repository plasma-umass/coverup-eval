# file thefuck/types.py:58-66
# lines [64, 65, 66]
# branches []

import pytest
from thefuck.types import Command

def test_command_update_missing_script_and_output():
    # Create an instance of Command with initial script and output
    command_instance = Command(script='initial_script', output='initial_output')
    
    # Call the update method without script and output to trigger lines 64-66
    updated_command = command_instance.update()
    
    # Assertions to verify the postconditions
    assert updated_command.script == 'initial_script'
    assert updated_command.output == 'initial_output'
