# file: lib/ansible/utils/context_objects.py:63-82
# asked: {"lines": [63, 64, 74, 75, 76, 77, 78, 80, 81, 82], "branches": [[76, 77], [76, 78]]}
# gained: {"lines": [63, 64, 74, 75, 76, 77, 78, 80, 81, 82], "branches": [[76, 77], [76, 78]]}

import pytest
from ansible.utils.context_objects import CLIArgs
from ansible.module_utils.common.collections import ImmutableDict

def _make_immutable(value):
    if isinstance(value, dict):
        return ImmutableDict(value)
    elif isinstance(value, list):
        return tuple(value)
    return value

def test_cliargs_init():
    mapping = {'key1': 'value1', 'key2': {'subkey': 'subvalue'}, 'key3': [1, 2, 3]}
    cli_args = CLIArgs(mapping)
    
    assert isinstance(cli_args, ImmutableDict)
    assert cli_args['key1'] == 'value1'
    assert isinstance(cli_args['key2'], ImmutableDict)
    assert cli_args['key2']['subkey'] == 'subvalue'
    assert isinstance(cli_args['key3'], tuple)
    assert cli_args['key3'] == (1, 2, 3)

def test_cliargs_from_options():
    class Options:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    
    options = Options(key1='value1', key2={'subkey': 'subvalue'}, key3=[1, 2, 3])
    cli_args = CLIArgs.from_options(options)
    
    assert isinstance(cli_args, ImmutableDict)
    assert cli_args['key1'] == 'value1'
    assert isinstance(cli_args['key2'], ImmutableDict)
    assert cli_args['key2']['subkey'] == 'subvalue'
    assert isinstance(cli_args['key3'], tuple)
    assert cli_args['key3'] == (1, 2, 3)
