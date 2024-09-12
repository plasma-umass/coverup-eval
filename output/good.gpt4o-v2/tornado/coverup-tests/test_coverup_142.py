# file: tornado/options.py:160-161
# asked: {"lines": [160, 161], "branches": []}
# gained: {"lines": [160, 161], "branches": []}

import pytest
from tornado.options import OptionParser

def test_option_parser_iter():
    parser = OptionParser()
    parser.define('test_option', default=42, help='A test option')
    
    # Ensure the option is defined
    assert 'test_option' in parser
    
    # Collect all option names using the iterator
    option_names = list(iter(parser))
    
    # Check that 'test_option' is in the collected option names
    assert 'test_option' in option_names
