# file docstring_parser/rest.py:21-83
# lines [21, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 41, 42, 44, 45, 46, 47, 48, 49, 50, 53, 54, 55, 56, 57, 59, 60, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 76, 77, 79, 80, 83]
# branches ['24->25', '24->53', '25->26', '25->32', '27->28', '27->31', '32->33', '32->37', '53->54', '53->70', '54->55', '54->56', '56->57', '56->59', '70->71', '70->83', '71->72', '71->73', '73->74', '73->76']

import pytest
from docstring_parser.rest import _build_meta, DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises, ParseError

def test_build_meta_param_keyword_with_type_and_optional():
    args = ["param", "int?", "x"]
    desc = "An integer parameter, defaults to 0."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.args == args
    assert result.description == desc
    assert result.arg_name == "x"
    assert result.type_name == "int"
    assert result.is_optional is True
    assert result.default == "0"

def test_build_meta_param_keyword_with_type():
    args = ["param", "int", "x"]
    desc = "An integer parameter."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.args == args
    assert result.description == desc
    assert result.arg_name == "x"
    assert result.type_name == "int"
    assert result.is_optional is False
    assert result.default is None

def test_build_meta_param_keyword_without_type():
    args = ["param", "x"]
    desc = "A parameter."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.args == args
    assert result.description == desc
    assert result.arg_name == "x"
    assert result.type_name is None
    assert result.is_optional is None
    assert result.default is None

def test_build_meta_param_keyword_invalid_args():
    args = ["param"]
    desc = "A parameter."
    with pytest.raises(ParseError, match="Expected one or two arguments for a param keyword."):
        _build_meta(args, desc)

def test_build_meta_returns_keyword_with_type():
    args = ["returns", "int"]
    desc = "Returns an integer."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.args == args
    assert result.description == desc
    assert result.type_name == "int"
    assert result.is_generator is False

def test_build_meta_returns_keyword_without_type():
    args = ["returns"]
    desc = "Returns a value."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.args == args
    assert result.description == desc
    assert result.type_name is None
    assert result.is_generator is False

def test_build_meta_returns_keyword_invalid_args():
    args = ["returns", "int", "extra"]
    desc = "Returns an integer."
    with pytest.raises(ParseError, match="Expected one or no arguments for a returns keyword."):
        _build_meta(args, desc)

def test_build_meta_raises_keyword_with_type():
    args = ["raises", "ValueError"]
    desc = "Raises a ValueError."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringRaises)
    assert result.args == args
    assert result.description == desc
    assert result.type_name == "ValueError"

def test_build_meta_raises_keyword_without_type():
    args = ["raises"]
    desc = "Raises an error."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringRaises)
    assert result.args == args
    assert result.description == desc
    assert result.type_name is None

def test_build_meta_raises_keyword_invalid_args():
    args = ["raises", "ValueError", "extra"]
    desc = "Raises a ValueError."
    with pytest.raises(ParseError, match="Expected one or no arguments for a raises keyword."):
        _build_meta(args, desc)

def test_build_meta_unknown_keyword():
    args = ["unknown"]
    desc = "An unknown keyword."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringMeta)
    assert result.args == args
    assert result.description == desc
