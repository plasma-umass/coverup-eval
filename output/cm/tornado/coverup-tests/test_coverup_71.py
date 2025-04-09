# file tornado/options.py:134-143
# lines [134, 136, 137, 138, 139, 140, 141, 142]
# branches []

import pytest
from tornado.options import OptionParser

# Test function to execute the missing lines/branches in OptionParser.__init__
def test_option_parser_init(mocker):
    # Mock the define method to assert it's called with expected arguments
    mock_define = mocker.patch.object(OptionParser, 'define', autospec=True)

    # Instantiate OptionParser to trigger __init__
    parser = OptionParser()

    # Assert that the define method was called with the correct parameters
    mock_define.assert_called_once_with(
        mocker.ANY,  # The self argument, which is the instance of OptionParser
        "help",
        type=bool,
        help="show this help information",
        callback=parser._help_callback
    )

    # Assert that the _options and _parse_callbacks are initialized as empty
    assert parser._options == {}
    assert parser._parse_callbacks == []

    # Clean up by deleting the parser instance
    del parser
