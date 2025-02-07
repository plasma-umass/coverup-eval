# file: lib/ansible/context.py:32-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest
from ansible.context import _init_global_context, CLIARGS
from ansible.utils.context_objects import GlobalCLIArgs

def test_init_global_context():
    cli_args = type('test', (object,), {'option1': 'value1', 'option2': 'value2'})()
    
    # Ensure CLIARGS is initially empty or has default values
    assert CLIARGS == GlobalCLIArgs({})
    
    # Initialize global context with test cli_args
    _init_global_context(cli_args)
    
    # Verify that CLIARGS is updated correctly
    assert CLIARGS == GlobalCLIArgs.from_options(cli_args)
    
    # Clean up by resetting CLIARGS to its default state
    default_cli_args = type('test', (object,), {})()
    _init_global_context(default_cli_args)
