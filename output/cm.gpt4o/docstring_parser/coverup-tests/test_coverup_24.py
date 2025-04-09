# file docstring_parser/numpydoc.py:281-323
# lines [288, 299, 300]
# branches ['287->288', '295->299', '305->313']

import pytest
from docstring_parser.numpydoc import NumpydocParser, Docstring

def test_numpydoc_parser_empty_text():
    parser = NumpydocParser()
    result = parser.parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None

def test_numpydoc_parser_no_titles():
    parser = NumpydocParser()
    text = "This is a description without any titles."
    result = parser.parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == "This is a description without any titles."
    assert result.long_description is None

def test_numpydoc_parser_long_description():
    parser = NumpydocParser()
    text = "Short description.\n\nLong description."
    result = parser.parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.blank_after_short_description
    assert not result.blank_after_long_description

def test_numpydoc_parser_with_titles(mocker):
    parser = NumpydocParser()
    text = "Short description.\n\nParameters\n----------\nparam1 : int\n    Description of param1."
    mocker.patch.object(parser, 'titles_re', mocker.Mock())
    parser.titles_re.search.return_value = mocker.Mock(start=lambda: 20)
    parser.titles_re.finditer.return_value = iter([mocker.Mock(groups=lambda: ["Parameters"], end=lambda: 30)])
    parser.sections = {"Parameters": mocker.Mock(parse=lambda x: ["parsed section"])}
    
    result = parser.parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.meta == ["parsed section"]
