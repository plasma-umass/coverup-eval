# file: tornado/options.py:160-161
# asked: {"lines": [161], "branches": []}
# gained: {"lines": [161], "branches": []}

import pytest
from unittest.mock import MagicMock

from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    mock_option1 = MagicMock()
    mock_option1.name = 'option1'
    mock_option2 = MagicMock()
    mock_option2.name = 'option2'
    parser.__dict__['_options'] = {
        'option1': mock_option1,
        'option2': mock_option2
    }
    return parser

def test_option_parser_iter(option_parser):
    options = list(option_parser)
    assert options == ['option1', 'option2']
