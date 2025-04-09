# file: tornado/options.py:167-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_option_parser_getitem(monkeypatch, option_parser):
    # Mock the __getattr__ method to ensure it is called
    def mock_getattr(self, name):
        return f"mocked_{name}"
    
    monkeypatch.setattr(OptionParser, "__getattr__", mock_getattr)
    
    # Test __getitem__ method
    result = option_parser["test_option"]
    
    # Assert that the result is as expected
    assert result == "mocked_test_option"
