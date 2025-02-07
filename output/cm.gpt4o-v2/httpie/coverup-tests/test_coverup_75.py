# file: httpie/cli/requestitems.py:87-88
# asked: {"lines": [87, 88], "branches": []}
# gained: {"lines": [87, 88], "branches": []}

import pytest
from httpie.cli.requestitems import process_header_arg
from httpie.cli.argtypes import KeyValueArg

def test_process_header_arg_with_value():
    arg = KeyValueArg(key='Content-Type', value='application/json', sep=':', orig='Content-Type:application/json')
    result = process_header_arg(arg)
    assert result == 'application/json'

def test_process_header_arg_without_value():
    arg = KeyValueArg(key='Content-Type', value=None, sep=':', orig='Content-Type:')
    result = process_header_arg(arg)
    assert result is None
