# file lib/ansible/utils/context_objects.py:85-92
# lines [85, 86, 87, 92]
# branches []

import pytest
from ansible.utils.context_objects import GlobalCLIArgs, CLIArgs

def test_global_cli_args_singleton(mocker):
    # Mock the _ABCSingleton to ensure the singleton behavior is tested
    mock_singleton = mocker.patch('ansible.utils.context_objects._ABCSingleton', autospec=True)
    
    # Mock the CLIArgs __init__ method to bypass the required argument
    mocker.patch.object(CLIArgs, '__init__', lambda self, mapping=None: None)
    
    # Create two instances of GlobalCLIArgs
    instance1 = GlobalCLIArgs()
    instance2 = GlobalCLIArgs()
    
    # Assert that both instances are the same, ensuring singleton behavior
    assert instance1 is instance2
    
    # Assert that GlobalCLIArgs is a subclass of CLIArgs
    assert issubclass(GlobalCLIArgs, CLIArgs)
    
    # Clean up by resetting the mock
    mock_singleton.reset_mock()
