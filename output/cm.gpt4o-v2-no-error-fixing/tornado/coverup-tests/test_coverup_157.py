# file: tornado/options.py:160-161
# asked: {"lines": [161], "branches": []}
# gained: {"lines": [161], "branches": []}

import pytest
from tornado.options import OptionParser

def test_optionparser_iter():
    parser = OptionParser()
    parser.define('test_option', default=42, type=int, help='test option')
    
    # Ensure the option is defined
    assert 'test_option' in parser
    
    # Collect all option names using the __iter__ method
    option_names = list(iter(parser))
    
    # Check that 'test_option' is in the list of option names
    assert 'test_option' in option_names
