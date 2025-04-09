# file docstring_parser/google.py:116-130
# lines [116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 128, 129, 130]
# branches ['117->118', '117->124', '124->125', '124->128', '128->129', '128->130']

import pytest
from docstring_parser import ParseError
from docstring_parser.google import GoogleParser, DocstringMeta, DocstringReturns, DocstringRaises

# Constants representing different keywords
RETURNS_KEYWORDS = {"returns", "return"}
YIELDS_KEYWORDS = {"yields", "yield"}
RAISES_KEYWORDS = {"raises", "raise"}
PARAM_KEYWORDS = {"param", "parameter", "arg", "argument", "key", "keyword"}

class Section:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

@pytest.fixture
def google_parser():
    return GoogleParser()

def test_build_single_meta_returns(google_parser):
    section = Section(key="return", value="")
    desc = "A return description"
    meta = google_parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringReturns)
    assert meta.args == ["return"]
    assert meta.description == desc
    assert meta.type_name is None
    assert not meta.is_generator

def test_build_single_meta_yields(google_parser):
    section = Section(key="yield", value="")
    desc = "A yield description"
    meta = google_parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringReturns)
    assert meta.args == ["yield"]
    assert meta.description == desc
    assert meta.type_name is None
    assert meta.is_generator

def test_build_single_meta_raises(google_parser):
    section = Section(key="raise", value="")
    desc = "A raise description"
    meta = google_parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringRaises)
    assert meta.args == ["raise"]
    assert meta.description == desc
    assert meta.type_name is None

def test_build_single_meta_param_error(google_parser):
    section = Section(key="param", value="")
    desc = "A param description"
    with pytest.raises(ParseError) as exc_info:
        google_parser._build_single_meta(section, desc)
    assert "Expected paramenter name." in str(exc_info.value)

def test_build_single_meta_generic(google_parser):
    section = Section(key="example", value="")
    desc = "A generic description"
    meta = google_parser._build_single_meta(section, desc)
    assert isinstance(meta, DocstringMeta)
    assert meta.args == ["example"]
    assert meta.description == desc
