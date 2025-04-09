# file: tornado/options.py:700-707
# asked: {"lines": [700, 701, 707], "branches": []}
# gained: {"lines": [700, 701, 707], "branches": []}

import pytest
from unittest import mock
from tornado.options import parse_command_line, options

@pytest.fixture
def mock_options_parse_command_line(monkeypatch):
    mock_func = mock.Mock(return_value=["arg1", "arg2"])
    monkeypatch.setattr(options.__class__, "parse_command_line", mock_func)
    return mock_func

def test_parse_command_line_with_args(mock_options_parse_command_line):
    args = ["--option1", "value1"]
    result = parse_command_line(args)
    mock_options_parse_command_line.assert_called_once_with(args, final=True)
    assert result == ["arg1", "arg2"]

def test_parse_command_line_without_args(mock_options_parse_command_line):
    result = parse_command_line()
    mock_options_parse_command_line.assert_called_once_with(None, final=True)
    assert result == ["arg1", "arg2"]

def test_parse_command_line_with_final_false(mock_options_parse_command_line):
    args = ["--option1", "value1"]
    result = parse_command_line(args, final=False)
    mock_options_parse_command_line.assert_called_once_with(args, final=False)
    assert result == ["arg1", "arg2"]
