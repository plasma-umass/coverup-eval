# file tornado/options.py:466-468
# lines [467, 468]
# branches ['467->exit', '467->468']

import pytest
from unittest.mock import Mock
from tornado.options import OptionParser

def test_run_parse_callbacks():
    parser = OptionParser()
    mock_callback = Mock()
    parser.add_parse_callback(mock_callback)
    parser.run_parse_callbacks()
    mock_callback.assert_called_once()
