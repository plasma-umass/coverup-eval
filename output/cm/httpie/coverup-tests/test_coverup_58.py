# file httpie/cli/requestitems.py:101-102
# lines [101, 102]
# branches []

import pytest
from httpie.cli.requestitems import KeyValueArg, process_query_param_arg

@pytest.fixture
def key_value_arg():
    return KeyValueArg(key='foo', value='bar', sep='=', orig='foo=bar')

def test_process_query_param_arg(key_value_arg):
    result = process_query_param_arg(key_value_arg)
    assert result == 'bar'
