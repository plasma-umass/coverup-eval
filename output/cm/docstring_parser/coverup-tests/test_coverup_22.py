# file docstring_parser/rest.py:21-83
# lines [21, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 41, 42, 44, 45, 46, 47, 48, 49, 50, 53, 54, 55, 56, 57, 59, 60, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 76, 77, 79, 80, 83]
# branches ['24->25', '24->53', '25->26', '25->32', '27->28', '27->31', '32->33', '32->37', '53->54', '53->70', '54->55', '54->56', '56->57', '56->59', '70->71', '70->83', '71->72', '71->73', '73->74', '73->76']

import pytest
from docstring_parser import ParseError, DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises
from docstring_parser.rest import _build_meta

PARAM_KEYWORDS = {"param", "parameter", "arg", "argument", "key", "keyword"}
RETURNS_KEYWORDS = {"return", "returns"}
YIELDS_KEYWORDS = {"yield", "yields"}
RAISES_KEYWORDS = {"raise", "raises", "except", "exception"}

def test_build_meta_param_with_default():
    args = ["param", "str?", "name"]
    desc = "description defaults to None."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "name"
    assert result.type_name == "str"
    assert result.is_optional is True
    assert result.default == "None"

def test_build_meta_param_without_type():
    args = ["param", "name"]
    desc = "description with no type."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "name"
    assert result.type_name is None
    assert result.is_optional is None
    assert result.default is None

def test_build_meta_param_incorrect_args():
    args = ["param"]
    desc = "description with missing args."
    with pytest.raises(ParseError):
        _build_meta(args, desc)

def test_build_meta_returns():
    args = ["return", "int"]
    desc = "description of return."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name == "int"
    assert result.is_generator is False

def test_build_meta_returns_no_type():
    args = ["return"]
    desc = "description of return with no type."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name is None
    assert result.is_generator is False

def test_build_meta_returns_incorrect_args():
    args = ["return", "int", "extra"]
    desc = "description with too many args."
    with pytest.raises(ParseError):
        _build_meta(args, desc)

def test_build_meta_yields():
    args = ["yield", "int"]
    desc = "description of yield."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name == "int"
    assert result.is_generator is True

def test_build_meta_raises():
    args = ["raise", "ValueError"]
    desc = "description of raise."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringRaises)
    assert result.type_name == "ValueError"

def test_build_meta_raises_no_type():
    args = ["raise"]
    desc = "description of raise with no type."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringRaises)
    assert result.type_name is None

def test_build_meta_raises_incorrect_args():
    args = ["raise", "ValueError", "extra"]
    desc = "description with too many args."
    with pytest.raises(ParseError):
        _build_meta(args, desc)

def test_build_meta_unknown_keyword():
    args = ["unknown", "arg"]
    desc = "description with unknown keyword."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringMeta)
    assert result.args == args
    assert result.description == desc
