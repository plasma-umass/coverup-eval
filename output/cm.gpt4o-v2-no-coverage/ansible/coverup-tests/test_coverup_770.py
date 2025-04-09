# file: lib/ansible/utils/context_objects.py:85-92
# asked: {"lines": [85, 86, 87, 92], "branches": []}
# gained: {"lines": [85, 86, 87, 92], "branches": []}

import pytest
from ansible.utils.context_objects import GlobalCLIArgs, CLIArgs

def test_global_cli_args_singleton():
    # Test that GlobalCLIArgs is a singleton
    args1 = GlobalCLIArgs({'arg1': 'value1'})
    args2 = GlobalCLIArgs({'arg2': 'value2'})
    
    assert args1 is args2
    assert args1['arg1'] == 'value1'
    assert 'arg2' not in args1

def test_cli_args_initialization():
    # Test the initialization of CLIArgs
    args = CLIArgs({'arg1': 'value1', 'arg2': 'value2'})
    
    assert args['arg1'] == 'value1'
    assert args['arg2'] == 'value2'

def test_cli_args_immutable():
    # Test that CLIArgs is immutable
    args = CLIArgs({'arg1': 'value1'})
    
    with pytest.raises(TypeError):
        args['arg1'] = 'new_value'
    
    with pytest.raises(AttributeError):
        args.update({'arg2': 'value2'})
