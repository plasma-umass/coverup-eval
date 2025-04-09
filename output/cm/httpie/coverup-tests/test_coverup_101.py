# file httpie/cli/requestitems.py:91-98
# lines [92, 93, 94, 96, 98]
# branches ['92->93', '92->98']

import pytest
from httpie.cli.exceptions import ParseError
from httpie.cli.requestitems import KeyValueArg, process_empty_header_arg

def test_process_empty_header_arg_with_non_empty_value():
    # Simulating a non-empty value
    key_value_arg = KeyValueArg(key='Header', value='non-empty', orig='Header:non-empty', sep=':')

    # Expecting a ParseError to be raised with a non-empty value
    with pytest.raises(ParseError) as exc_info:
        process_empty_header_arg(key_value_arg)

    # Verifying the exception message
    assert str(exc_info.value) == 'Invalid item "Header:non-empty" (to specify an empty header use `Header;`)'

def test_process_empty_header_arg_with_empty_value():
    # Simulating an empty value
    key_value_arg = KeyValueArg(key='Header', value='', orig='Header;', sep=';')

    # No exception should be raised with an empty value
    result = process_empty_header_arg(key_value_arg)

    # Verifying the result is an empty string
    assert result == ""
