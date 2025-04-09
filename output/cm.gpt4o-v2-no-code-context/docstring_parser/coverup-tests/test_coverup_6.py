# file: docstring_parser/google.py:269-274
# asked: {"lines": [269, 274], "branches": []}
# gained: {"lines": [269, 274], "branches": []}

import pytest
from docstring_parser.google import parse, GoogleParser
from docstring_parser.common import Docstring

def test_parse_google_style_docstring(monkeypatch):
    sample_docstring = """
    Summary of the function.

    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.

    Returns:
        bool: Description of return value.
    """

    def mock_parse(self, text):
        assert text == sample_docstring
        return Docstring()

    monkeypatch.setattr(GoogleParser, 'parse', mock_parse)
    result = parse(sample_docstring)
    assert isinstance(result, Docstring)
