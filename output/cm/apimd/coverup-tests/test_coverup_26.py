# file apimd/parser.py:564-574
# lines [564, 566, 567, 568, 569, 570, 571, 572, 574]
# branches ['567->568', '567->571', '568->567', '568->569', '571->572', '571->574']

import pytest
from apimd.parser import Parser
from unittest.mock import MagicMock

def test_parser_get_const_with_no_constants():
    # Create a Parser instance with a MagicMock
    parser = Parser()
    parser.root = {}
    parser.const = []
    parser.is_public = MagicMock(return_value=True)

    # Test __get_const with no constants
    result = parser._Parser__get_const("SOME_CONST")
    assert result == ""

def test_parser_get_const_with_constants(mocker):
    # Create a Parser instance with a MagicMock
    parser = Parser()
    parser.root = {'SOME_CONST.FOO': 'SOME_CONST', 'SOME_CONST.BAR': 'SOME_CONST', '_SOME_CONST.BAZ': 'SOME_CONST'}
    parser.const = {'SOME_CONST.FOO': 'FooType', 'SOME_CONST.BAR': 'BarType', '_SOME_CONST.BAZ': 'BazType'}
    parser.is_public = MagicMock(side_effect=lambda name: not name.startswith('_'))

    # Mock the code function to simply return the input string
    mocker.patch('apimd.parser.code', side_effect=lambda x: x)
    # Mock the table function to return a formatted string
    mocker.patch('apimd.parser.table', side_effect=lambda title, col, items: f"{title}-{col}-{items}")

    # Test __get_const with constants
    result = parser._Parser__get_const("SOME_CONST")
    assert result == "Constants-Type-[('FOO', 'FooType'), ('BAR', 'BarType')]"

# Run the tests
pytest.main()
