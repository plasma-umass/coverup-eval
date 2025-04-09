# file tornado/options.py:163-165
# lines [164, 165]
# branches []

import pytest
from tornado.options import OptionParser

class MockOptionParser(OptionParser):
    def __init__(self):
        object.__setattr__(self, '_options', {'test_option': 'value'})
    
    def _normalize_name(self, name):
        return name.lower()

@pytest.fixture
def mock_option_parser():
    return MockOptionParser()

def test_option_parser_contains(mock_option_parser):
    # Test with a name that exists in _options
    assert 'test_option' in mock_option_parser
    
    # Test with a name that does not exist in _options
    assert 'nonexistent_option' not in mock_option_parser
