# file: docstring_parser/google.py:132-173
# asked: {"lines": [138, 139, 140, 141, 142, 143, 144, 146, 162, 163, 164, 165, 166, 167, 169, 170, 171, 173], "branches": [[135, 162], [137, 138], [139, 140], [139, 142], [142, 143], [142, 146], [162, 163], [162, 169], [169, 170], [169, 173]]}
# gained: {"lines": [138, 139, 140, 141, 162, 163, 164, 165, 166, 167, 169, 170, 171, 173], "branches": [[135, 162], [137, 138], [139, 140], [162, 163], [162, 169], [169, 170], [169, 173]]}

import pytest
from docstring_parser.common import PARAM_KEYWORDS, RAISES_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns
from docstring_parser.google import GoogleParser
import re

# Mocking the regex patterns used in the GoogleParser class
GOOGLE_TYPED_ARG_REGEX = re.compile(r"(\w+)\s*\(([^)]+)\)")
GOOGLE_ARG_DESC_REGEX = re.compile(r".*Defaults to (.*)\.")

class Section:
    def __init__(self, key):
        self.key = key

@pytest.fixture
def parser():
    return GoogleParser()

def test_build_multi_meta_param(parser, mocker):
    section = Section(key="param")
    before = "param_name (str, optional)"
    desc = "This is a parameter. Defaults to None."
    
    mocker.patch('docstring_parser.google.GOOGLE_TYPED_ARG_REGEX', GOOGLE_TYPED_ARG_REGEX)
    mocker.patch('docstring_parser.google.GOOGLE_ARG_DESC_REGEX', GOOGLE_ARG_DESC_REGEX)
    
    result = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "param_name"
    assert result.type_name == "str"
    assert result.is_optional is True
    assert result.default == "None"
    assert result.description == desc

def test_build_multi_meta_returns(parser):
    section = Section(key="returns")
    before = "str"
    desc = "This is a return value."
    
    result = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(result, DocstringReturns)
    assert result.type_name == "str"
    assert result.is_generator is False
    assert result.description == desc

def test_build_multi_meta_yields(parser):
    section = Section(key="yields")
    before = "str"
    desc = "This is a yield value."
    
    result = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(result, DocstringReturns)
    assert result.type_name == "str"
    assert result.is_generator is True
    assert result.description == desc

def test_build_multi_meta_raises(parser):
    section = Section(key="raises")
    before = "ValueError"
    desc = "This is an exception."
    
    result = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(result, DocstringRaises)
    assert result.type_name == "ValueError"
    assert result.description == desc

def test_build_multi_meta_default(parser):
    section = Section(key="note")
    before = "Note"
    desc = "This is a note."
    
    result = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(result, DocstringMeta)
    assert result.args == ["note", "Note"]
    assert result.description == desc
