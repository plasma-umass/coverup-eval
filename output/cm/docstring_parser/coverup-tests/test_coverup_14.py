# file docstring_parser/numpydoc.py:266-270
# lines [266, 267, 268, 269]
# branches []

import pytest
import re
from docstring_parser.numpydoc import NumpydocParser

class TestNumpydocParser:
    def test_setup_titles_re(self, mocker):
        # Mocking the sections to have a title_pattern
        mock_section = mocker.Mock()
        mock_section.title_pattern = "Parameters"
        mock_sections = {'Parameters': mock_section}

        # Instantiate NumpydocParser and set the mock sections
        parser = NumpydocParser()
        mocker.patch.object(parser, 'sections', mock_sections)

        # Call the _setup method which should use the mocked sections
        parser._setup()

        # Assert that the titles_re is compiled correctly
        assert isinstance(parser.titles_re, re.Pattern)
        assert "Parameters" in parser.titles_re.pattern
