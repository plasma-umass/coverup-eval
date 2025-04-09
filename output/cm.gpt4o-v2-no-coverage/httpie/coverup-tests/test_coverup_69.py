# file: httpie/cli/requestitems.py:120-121
# asked: {"lines": [120, 121], "branches": []}
# gained: {"lines": [120, 121], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_item_arg

def test_process_data_item_arg():
    # Test with a normal value
    arg = KeyValueArg(key='test', value='value', sep='=', orig='test=value')
    assert process_data_item_arg(arg) == 'value'

    # Test with a None value
    arg = KeyValueArg(key='test', value=None, sep='=', orig='test=')
    assert process_data_item_arg(arg) is None
