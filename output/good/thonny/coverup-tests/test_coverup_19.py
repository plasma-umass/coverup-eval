# file thonny/roughparse.py:621-628
# lines [621, 622, 623, 624, 625, 626, 627, 628]
# branches ['626->627', '626->628']

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    @pytest.fixture
    def parser(self, mocker):
        mocker.patch.object(RoughParser, '_study2')
        # Provide the required arguments for RoughParser initialization
        return RoughParser(indent_width=4, tabwidth=4)

    def test_get_base_indent_string(self, parser):
        # Setup the parser object with necessary attributes
        parser.str = "    indented line"
        parser.stmt_start = 0
        parser.stmt_end = len(parser.str)

        # Call the method under test
        indent_str = parser.get_base_indent_string()

        # Assert that the method returns the correct base indent string
        assert indent_str == "    ", "The base indent string should be four spaces"

    def test_get_base_indent_string_with_tabs(self, parser):
        # Setup the parser object with necessary attributes
        parser.str = "\t\tindented line"
        parser.stmt_start = 0
        parser.stmt_end = len(parser.str)

        # Call the method under test
        indent_str = parser.get_base_indent_string()

        # Assert that the method returns the correct base indent string
        assert indent_str == "\t\t", "The base indent string should be two tabs"

    def test_get_base_indent_string_no_indent(self, parser):
        # Setup the parser object with necessary attributes
        parser.str = "no indent"
        parser.stmt_start = 0
        parser.stmt_end = len(parser.str)

        # Call the method under test
        indent_str = parser.get_base_indent_string()

        # Assert that the method returns an empty string for no indent
        assert indent_str == "", "The base indent string should be empty for no indent"
