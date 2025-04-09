# file: httpie/cli/requestitems.py:101-102
# asked: {"lines": [101, 102], "branches": []}
# gained: {"lines": [101, 102], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_query_param_arg

def test_process_query_param_arg():
    # Test with a normal value
    arg = KeyValueArg(key='key', value='value', sep='=', orig='key=value')
    assert process_query_param_arg(arg) == 'value'

    # Test with a None value
    arg = KeyValueArg(key='key', value=None, sep='=', orig='key=')
    assert process_query_param_arg(arg) is None
