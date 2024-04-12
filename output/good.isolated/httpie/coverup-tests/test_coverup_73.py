# file httpie/cli/requestitems.py:87-88
# lines [87, 88]
# branches []

import pytest
from httpie.cli.requestitems import KeyValueArg, process_header_arg

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_process_header_arg_with_value():
    # Test with a KeyValueArg that has a value
    arg_with_value = KeyValueArg(key='Header', value='Value', sep=':', orig='Header:Value')
    assert process_header_arg(arg_with_value) == 'Value'

def test_process_header_arg_without_value():
    # Test with a KeyValueArg that has no value
    arg_without_value = KeyValueArg(key='Header', value=None, sep=':', orig='Header:')
    assert process_header_arg(arg_without_value) is None
