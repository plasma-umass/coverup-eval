# file: tornado/options.py:134-143
# asked: {"lines": [134, 136, 137, 138, 139, 140, 141, 142], "branches": []}
# gained: {"lines": [134, 136, 137, 138, 139, 140, 141, 142], "branches": []}

import pytest
from tornado.options import OptionParser

def test_option_parser_initialization():
    parser = OptionParser()
    
    # Verify that _options and _parse_callbacks are initialized correctly
    assert 'help' in parser._options
    assert parser._parse_callbacks == []

    # Verify that the 'help' option is defined correctly
    help_option = parser._options['help']
    assert help_option.type == bool
    assert help_option.help == "show this help information"
    assert help_option.callback == parser._help_callback

@pytest.fixture(autouse=True)
def cleanup_option_parser():
    yield
    OptionParser()._options.clear()
    OptionParser()._parse_callbacks.clear()
