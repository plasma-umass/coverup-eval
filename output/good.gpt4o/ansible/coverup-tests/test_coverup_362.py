# file lib/ansible/utils/context_objects.py:63-82
# lines [63, 64, 74, 75, 76, 77, 78, 80, 81, 82]
# branches ['76->77', '76->78']

import pytest
from ansible.utils.context_objects import CLIArgs

class MockOptions:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def test_cliargs_initialization():
    mapping = {'arg1': 'value1', 'arg2': 'value2'}
    cli_args = CLIArgs(mapping)
    
    assert cli_args['arg1'] == 'value1'
    assert cli_args['arg2'] == 'value2'

def test_cliargs_from_options():
    options = MockOptions(arg1='value1', arg2='value2')
    cli_args = CLIArgs.from_options(options)
    
    assert cli_args['arg1'] == 'value1'
    assert cli_args['arg2'] == 'value2'
