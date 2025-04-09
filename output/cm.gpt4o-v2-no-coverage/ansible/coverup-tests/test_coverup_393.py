# file: lib/ansible/utils/context_objects.py:63-82
# asked: {"lines": [63, 64, 74, 75, 76, 77, 78, 80, 81, 82], "branches": [[76, 77], [76, 78]]}
# gained: {"lines": [63, 64, 74, 75, 76, 77, 78, 80, 81, 82], "branches": [[76, 77], [76, 78]]}

import pytest
from ansible.utils.context_objects import CLIArgs
from ansible.module_utils.common.collections import ImmutableDict

class MockOptions:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def test_cliargs_init():
    mapping = {'key1': 'value1', 'key2': {'subkey': 'subvalue'}}
    cli_args = CLIArgs(mapping)
    assert isinstance(cli_args, ImmutableDict)
    assert cli_args['key1'] == 'value1'
    assert isinstance(cli_args['key2'], ImmutableDict)
    assert cli_args['key2']['subkey'] == 'subvalue'

def test_cliargs_from_options():
    options = MockOptions(key1='value1', key2={'subkey': 'subvalue'})
    cli_args = CLIArgs.from_options(options)
    assert isinstance(cli_args, ImmutableDict)
    assert cli_args['key1'] == 'value1'
    assert isinstance(cli_args['key2'], ImmutableDict)
    assert cli_args['key2']['subkey'] == 'subvalue'
