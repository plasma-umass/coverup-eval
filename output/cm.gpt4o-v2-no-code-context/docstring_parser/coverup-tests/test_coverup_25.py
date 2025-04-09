# file: docstring_parser/google.py:116-130
# asked: {"lines": [117, 118, 119, 120, 121, 122, 124, 125, 126, 128, 129, 130], "branches": [[117, 118], [117, 124], [124, 125], [124, 128], [128, 129], [128, 130]]}
# gained: {"lines": [117, 118, 119, 120, 121, 122, 124, 125, 126, 128, 129, 130], "branches": [[117, 118], [117, 124], [124, 125], [124, 128], [128, 129], [128, 130]]}

import pytest
from docstring_parser.google import GoogleParser, Section, DocstringMeta, DocstringReturns, DocstringRaises, ParseError

RETURNS_KEYWORDS = {"return", "returns"}
YIELDS_KEYWORDS = {"yield", "yields"}
RAISES_KEYWORDS = {"raise", "raises"}
PARAM_KEYWORDS = {"param", "parameter"}

@pytest.fixture
def parser():
    return GoogleParser()

def test_build_single_meta_returns(parser):
    section = Section(key="return", title="", type="")
    desc = "This is a return description."
    result = parser._build_single_meta(section, desc)
    assert isinstance(result, DocstringReturns)
    assert result.args == ["return"]
    assert result.description == desc
    assert result.type_name is None
    assert not result.is_generator

def test_build_single_meta_yields(parser):
    section = Section(key="yield", title="", type="")
    desc = "This is a yield description."
    result = parser._build_single_meta(section, desc)
    assert isinstance(result, DocstringReturns)
    assert result.args == ["yield"]
    assert result.description == desc
    assert result.type_name is None
    assert result.is_generator

def test_build_single_meta_raises(parser):
    section = Section(key="raise", title="", type="")
    desc = "This is a raise description."
    result = parser._build_single_meta(section, desc)
    assert isinstance(result, DocstringRaises)
    assert result.args == ["raise"]
    assert result.description == desc
    assert result.type_name is None

def test_build_single_meta_param_error(parser):
    section = Section(key="param", title="", type="")
    desc = "This is a param description."
    with pytest.raises(ParseError, match="Expected paramenter name."):
        parser._build_single_meta(section, desc)

def test_build_single_meta_default(parser):
    section = Section(key="other", title="", type="")
    desc = "This is a default description."
    result = parser._build_single_meta(section, desc)
    assert isinstance(result, DocstringMeta)
    assert result.args == ["other"]
    assert result.description == desc
