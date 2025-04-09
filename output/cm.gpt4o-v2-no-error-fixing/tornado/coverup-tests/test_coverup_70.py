# file: tornado/options.py:466-468
# asked: {"lines": [466, 467, 468], "branches": [[467, 0], [467, 468]]}
# gained: {"lines": [466, 467, 468], "branches": [[467, 0], [467, 468]]}

import pytest
from unittest.mock import Mock
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_run_parse_callbacks(option_parser):
    mock_callback = Mock()
    option_parser.add_parse_callback(mock_callback)
    
    option_parser.run_parse_callbacks()
    
    mock_callback.assert_called_once()

