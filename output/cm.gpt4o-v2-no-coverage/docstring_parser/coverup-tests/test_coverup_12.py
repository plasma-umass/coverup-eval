# file: docstring_parser/google.py:116-130
# asked: {"lines": [116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 128, 129, 130], "branches": [[117, 118], [117, 124], [124, 125], [124, 128], [128, 129], [128, 130]]}
# gained: {"lines": [116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 128, 129, 130], "branches": [[117, 118], [117, 124], [124, 125], [124, 128], [128, 129], [128, 130]]}

import pytest
from docstring_parser.common import PARAM_KEYWORDS, RAISES_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, DocstringMeta, DocstringRaises, DocstringReturns, ParseError
from docstring_parser.google import GoogleParser

class Section:
    def __init__(self, key):
        self.key = key

@pytest.fixture
def parser():
    return GoogleParser()

def test_build_single_meta_returns(parser):
    section = Section(key='return')
    desc = "This is a return description."
    result = parser._build_single_meta(section, desc)
    assert isinstance(result, DocstringReturns)
    assert result.args == ['return']
    assert result.description == desc
    assert result.type_name is None
    assert result.is_generator is False

def test_build_single_meta_yields(parser):
    section = Section(key='yield')
    desc = "This is a yield description."
    result = parser._build_single_meta(section, desc)
    assert isinstance(result, DocstringReturns)
    assert result.args == ['yield']
    assert result.description == desc
    assert result.type_name is None
    assert result.is_generator is True

def test_build_single_meta_raises(parser):
    section = Section(key='raises')
    desc = "This is a raises description."
    result = parser._build_single_meta(section, desc)
    assert isinstance(result, DocstringRaises)
    assert result.args == ['raises']
    assert result.description == desc
    assert result.type_name is None

def test_build_single_meta_param_error(parser):
    section = Section(key='param')
    desc = "This is a param description."
    with pytest.raises(ParseError, match="Expected paramenter name."):
        parser._build_single_meta(section, desc)

def test_build_single_meta_default(parser):
    section = Section(key='other')
    desc = "This is a default description."
    result = parser._build_single_meta(section, desc)
    assert isinstance(result, DocstringMeta)
    assert result.args == ['other']
    assert result.description == desc
