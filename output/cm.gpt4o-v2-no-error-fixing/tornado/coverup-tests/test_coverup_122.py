# file: tornado/options.py:210-215
# asked: {"lines": [210, 215], "branches": []}
# gained: {"lines": [210, 215], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    # Clean up if necessary

def test_as_dict(option_parser):
    option_parser.define('test_option', default=42, type=int, help='A test option')
    option_parser.define('another_option', default='default', type=str, help='Another test option')
    
    options_dict = option_parser.as_dict()
    
    assert 'test_option' in options_dict
    assert options_dict['test_option'] == 42
    assert 'another_option' in options_dict
    assert options_dict['another_option'] == 'default'
