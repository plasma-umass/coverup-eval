# file: tornado/options.py:726-731
# asked: {"lines": [726, 731], "branches": []}
# gained: {"lines": [726, 731], "branches": []}

import pytest
from unittest.mock import Mock
from tornado.options import add_parse_callback, OptionParser

@pytest.fixture
def mock_option_parser(monkeypatch):
    mock_parser = Mock(spec=OptionParser)
    monkeypatch.setattr('tornado.options.options', mock_parser)
    return mock_parser

def test_add_parse_callback(mock_option_parser):
    callback = Mock()
    add_parse_callback(callback)
    mock_option_parser.add_parse_callback.assert_called_once_with(callback)
