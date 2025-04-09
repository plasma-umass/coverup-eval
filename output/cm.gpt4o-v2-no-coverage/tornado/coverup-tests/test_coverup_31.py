# file: tornado/options.py:304-356
# asked: {"lines": [304, 305, 328, 329, 330, 331, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 350, 351, 353, 354, 356], "branches": [[328, 329], [328, 330], [331, 333], [331, 353], [333, 334], [333, 336], [336, 337], [336, 339], [342, 343], [342, 345], [346, 347], [346, 351], [347, 348], [347, 350], [353, 354], [353, 356]]}
# gained: {"lines": [304, 305, 328, 329, 330, 331, 333, 334, 335, 336, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 350, 351, 353, 354, 356], "branches": [[328, 329], [328, 330], [331, 333], [331, 353], [333, 334], [333, 336], [336, 339], [342, 343], [342, 345], [346, 347], [346, 351], [347, 348], [347, 350], [353, 354], [353, 356]]}

import pytest
from unittest.mock import MagicMock, patch

class MockOption:
    def __init__(self, name, type, multiple=False, metavar=None, help=None, default=None):
        self.name = name
        self.type = type
        self.multiple = multiple
        self.metavar = metavar
        self.help = help
        self.default = default

    def parse(self, value):
        pass

class MockError(Exception):
    pass

@pytest.fixture
def option_parser(monkeypatch):
    from tornado.options import OptionParser

    parser = OptionParser()
    parser.define('bool_option', type=bool)
    parser.define('int_option', type=int)
    parser.define('str_option', type=str)
    parser._parse_callbacks.append(MagicMock())
    monkeypatch.setattr('tornado.options.Error', MockError)
    return parser

def test_parse_command_line_no_args(option_parser):
    with patch('sys.argv', ['program']):
        remaining = option_parser.parse_command_line()
        assert remaining == []

def test_parse_command_line_with_args(option_parser):
    args = ['program', '--bool_option', '--int_option=10', '--str_option=test', 'arg1', 'arg2']
    remaining = option_parser.parse_command_line(args)
    assert remaining == ['arg1', 'arg2']

def test_parse_command_line_unrecognized_option(option_parser):
    args = ['program', '--unknown_option']
    with pytest.raises(MockError, match="Unrecognized command line option: 'unknown-option'"):
        option_parser.parse_command_line(args)

def test_parse_command_line_option_requires_value(option_parser):
    args = ['program', '--int_option']
    with pytest.raises(MockError, match="Option 'int-option' requires a value"):
        option_parser.parse_command_line(args)

def test_parse_command_line_final_false(option_parser):
    args = ['program', '--bool_option']
    remaining = option_parser.parse_command_line(args, final=False)
    assert remaining == []
    option_parser._parse_callbacks[0].assert_not_called()

def test_parse_command_line_final_true(option_parser):
    args = ['program', '--bool_option']
    remaining = option_parser.parse_command_line(args, final=True)
    assert remaining == []
    option_parser._parse_callbacks[0].assert_called_once()
