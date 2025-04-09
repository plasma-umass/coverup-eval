# file: tornado/options.py:173-178
# asked: {"lines": [173, 178], "branches": []}
# gained: {"lines": [173, 178], "branches": []}

import pytest
from unittest.mock import Mock

from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    # Clean up if necessary

def test_items(option_parser):
    mock_option = Mock()
    mock_option.name = 'test_option'
    mock_option.value.return_value = 'test_value'
    
    option_parser.__dict__['_options'] = {'test_option': mock_option}
    
    items = list(option_parser.items())
    
    assert items == [('test_option', 'test_value')]
    mock_option.value.assert_called_once()
