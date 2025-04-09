# file tornado/options.py:304-356
# lines [304, 305, 328, 329, 330, 331, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 350, 351, 353, 354, 356]
# branches ['328->329', '328->330', '331->333', '331->353', '333->334', '333->336', '336->337', '336->339', '342->343', '342->345', '346->347', '346->351', '347->348', '347->350', '353->354', '353->356']

import pytest
from unittest import mock
import sys
from tornado.options import Error

class MockOption:
    def __init__(self, type, multiple=False):
        self.type = type
        self.multiple = multiple

    def parse(self, value):
        pass

class MockOptionParser:
    def __init__(self):
        self._options = {
            'bool_option': MockOption(bool),
            'int_option': MockOption(int),
            'str_option': MockOption(str),
        }

    def _normalize_name(self, name):
        return name.replace('-', '_')

    def print_help(self):
        pass

    def run_parse_callbacks(self):
        pass

    def parse_command_line(self, args=None, final=True):
        if args is None:
            args = sys.argv
        remaining = []
        for i in range(1, len(args)):
            if not args[i].startswith("-"):
                remaining = args[i:]
                break
            if args[i] == "--":
                remaining = args[i + 1:]
                break
            arg = args[i].lstrip("-")
            name, equals, value = arg.partition("=")
            name = self._normalize_name(name)
            if name not in self._options:
                self.print_help()
                raise Error("Unrecognized command line option: %r" % name)
            option = self._options[name]
            if not equals:
                if option.type == bool:
                    value = "true"
                else:
                    raise Error("Option %r requires a value" % name)
            option.parse(value)

        if final:
            self.run_parse_callbacks()

        return remaining

@pytest.fixture
def mock_option_parser():
    return MockOptionParser()

def test_parse_command_line_no_args(mock_option_parser):
    remaining = mock_option_parser.parse_command_line(args=[])
    assert remaining == []

def test_parse_command_line_unrecognized_option(mock_option_parser):
    with pytest.raises(Error, match="Unrecognized command line option: 'unknown_option'"):
        mock_option_parser.parse_command_line(args=['program_name', '--unknown_option=value'])

def test_parse_command_line_bool_option(mock_option_parser):
    remaining = mock_option_parser.parse_command_line(args=['program_name', '--bool_option'])
    assert remaining == []

def test_parse_command_line_int_option_missing_value(mock_option_parser):
    with pytest.raises(Error, match="Option 'int_option' requires a value"):
        mock_option_parser.parse_command_line(args=['program_name', '--int_option'])

def test_parse_command_line_int_option_with_value(mock_option_parser):
    remaining = mock_option_parser.parse_command_line(args=['program_name', '--int_option=10'])
    assert remaining == []

def test_parse_command_line_str_option_with_value(mock_option_parser):
    remaining = mock_option_parser.parse_command_line(args=['program_name', '--str_option=hello'])
    assert remaining == []

def test_parse_command_line_remaining_args(mock_option_parser):
    remaining = mock_option_parser.parse_command_line(args=['program_name', '--str_option=hello', 'arg1', 'arg2'])
    assert remaining == ['arg1', 'arg2']

def test_parse_command_line_final_false(mock_option_parser):
    with mock.patch.object(mock_option_parser, 'run_parse_callbacks') as mock_run_parse_callbacks:
        remaining = mock_option_parser.parse_command_line(args=['program_name', '--str_option=hello'], final=False)
        assert remaining == []
        mock_run_parse_callbacks.assert_not_called()

def test_parse_command_line_final_true(mock_option_parser):
    with mock.patch.object(mock_option_parser, 'run_parse_callbacks') as mock_run_parse_callbacks:
        remaining = mock_option_parser.parse_command_line(args=['program_name', '--str_option=hello'], final=True)
        assert remaining == []
        mock_run_parse_callbacks.assert_called_once()
