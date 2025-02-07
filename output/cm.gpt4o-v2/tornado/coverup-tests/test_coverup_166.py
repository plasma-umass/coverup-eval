# file: tornado/options.py:173-178
# asked: {"lines": [173, 178], "branches": []}
# gained: {"lines": [173, 178], "branches": []}

import pytest
from unittest.mock import MagicMock
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    parser._options.clear()

def test_items(option_parser):
    mock_option = MagicMock()
    mock_option.name = "test_option"
    mock_option.value.return_value = "test_value"
    
    option_parser._options["test_option"] = mock_option
    
    items = list(option_parser.items())
    
    assert ("test_option", "test_value") in items
    mock_option.value.assert_called_once()
