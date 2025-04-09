# file docstring_parser/google.py:132-173
# lines [140, 141, 143, 144, 148, 149, 169, 170, 171, 173]
# branches ['137->148', '139->140', '142->143', '162->169', '169->170', '169->173']

import pytest
from docstring_parser.google import GoogleParser, Section, DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises

@pytest.fixture
def parser():
    return GoogleParser()

def test_build_multi_meta_param_optional_comma(parser):
    section = Section(key="param", title="", type="")
    before = "arg_name (int, optional)"
    desc = "description"
    result = parser._build_multi_meta(section, before, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "arg_name"
    assert result.type_name == "int"
    assert result.is_optional is True

def test_build_multi_meta_param_optional_question(parser):
    section = Section(key="param", title="", type="")
    before = "arg_name (int?)"
    desc = "description"
    result = parser._build_multi_meta(section, before, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "arg_name"
    assert result.type_name == "int"
    assert result.is_optional is True

def test_build_multi_meta_param_no_type(parser):
    section = Section(key="param", title="", type="")
    before = "arg_name"
    desc = "description"
    result = parser._build_multi_meta(section, before, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "arg_name"
    assert result.type_name is None
    assert result.is_optional is None

def test_build_multi_meta_raises(parser):
    section = Section(key="raises", title="", type="")
    before = "Exception"
    desc = "description"
    result = parser._build_multi_meta(section, before, desc)
    assert isinstance(result, DocstringRaises)
    assert result.type_name == "Exception"

def test_build_multi_meta_default(parser):
    section = Section(key="unknown", title="", type="")
    before = "arg_name"
    desc = "description"
    result = parser._build_multi_meta(section, before, desc)
    assert isinstance(result, DocstringMeta)
    assert result.args == ["unknown", "arg_name"]
    assert result.description == "description"
