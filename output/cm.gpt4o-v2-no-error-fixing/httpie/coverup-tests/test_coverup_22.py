# file: httpie/cli/requestitems.py:91-98
# asked: {"lines": [91, 92, 93, 94, 96, 98], "branches": [[92, 93], [92, 98]]}
# gained: {"lines": [91, 92, 93, 94, 96, 98], "branches": [[92, 93], [92, 98]]}

import pytest
from httpie.cli.requestitems import process_empty_header_arg
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.exceptions import ParseError

def test_process_empty_header_arg_with_value():
    arg = KeyValueArg(key='Header', value='some_value', sep=':', orig='Header:some_value')
    with pytest.raises(ParseError) as excinfo:
        process_empty_header_arg(arg)
    assert 'Invalid item "Header:some_value" (to specify an empty header use `Header;`)' in str(excinfo.value)

def test_process_empty_header_arg_without_value():
    arg = KeyValueArg(key='Header', value=None, sep=':', orig='Header:')
    result = process_empty_header_arg(arg)
    assert result is None
