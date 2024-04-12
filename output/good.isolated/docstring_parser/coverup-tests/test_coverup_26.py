# file docstring_parser/parser.py:7-25
# lines [21, 22, 24]
# branches ['23->24']

import pytest
from docstring_parser.parser import parse, Style
from docstring_parser.common import ParseError

def test_parse_raises_exception(mocker):
    # Mock a parser function to raise ParseError
    mock_parser = mocker.Mock(side_effect=ParseError("Mocked parse error"))
    mocker.patch.dict('docstring_parser.parser.STYLES', {'mock_style': mock_parser}, clear=True)

    # Test that parse raises ParseError when all styles raise ParseError
    with pytest.raises(ParseError):
        parse("Some docstring", style=Style.auto)

    # Clean up by removing the mock from STYLES
    mocker.stopall()
