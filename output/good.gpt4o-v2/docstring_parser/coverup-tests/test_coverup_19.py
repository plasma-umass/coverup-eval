# file: docstring_parser/rest.py:21-83
# asked: {"lines": [21, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 41, 42, 44, 45, 46, 47, 48, 49, 50, 53, 54, 55, 56, 57, 59, 60, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 76, 77, 79, 80, 83], "branches": [[24, 25], [24, 53], [25, 26], [25, 32], [27, 28], [27, 31], [32, 33], [32, 37], [53, 54], [53, 70], [54, 55], [54, 56], [56, 57], [56, 59], [70, 71], [70, 83], [71, 72], [71, 73], [73, 74], [73, 76]]}
# gained: {"lines": [21, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 41, 42, 44, 45, 46, 47, 48, 49, 50, 53, 54, 55, 56, 57, 59, 60, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 76, 77, 79, 80, 83], "branches": [[24, 25], [24, 53], [25, 26], [25, 32], [27, 28], [27, 31], [32, 33], [32, 37], [53, 54], [53, 70], [54, 55], [54, 56], [56, 57], [56, 59], [70, 71], [70, 83], [71, 72], [71, 73], [73, 74], [73, 76]]}

import pytest
from docstring_parser.rest import _build_meta
from docstring_parser.common import ParseError, DocstringParam, DocstringReturns, DocstringRaises, DocstringMeta

def test_build_meta_param_with_type_and_optional():
    args = ["param", "str?", "arg"]
    desc = "This is a description."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "arg"
    assert result.type_name == "str"
    assert result.is_optional is True
    assert result.description == desc
    assert result.default is None

def test_build_meta_param_with_type_and_non_optional():
    args = ["param", "str", "arg"]
    desc = "This is a description."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "arg"
    assert result.type_name == "str"
    assert result.is_optional is False
    assert result.description == desc
    assert result.default is None

def test_build_meta_param_with_default():
    args = ["param", "str", "arg"]
    desc = "This is a description. defaults to 'default_value'."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "arg"
    assert result.type_name == "str"
    assert result.is_optional is False
    assert result.description == desc
    assert result.default == "'default_value'"

def test_build_meta_param_without_type():
    args = ["param", "arg"]
    desc = "This is a description."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "arg"
    assert result.type_name is None
    assert result.is_optional is None
    assert result.description == desc
    assert result.default is None

def test_build_meta_param_invalid_args():
    args = ["param"]
    desc = "This is a description."
    with pytest.raises(ParseError, match="Expected one or two arguments for a param keyword."):
        _build_meta(args, desc)

def test_build_meta_returns_with_type():
    args = ["returns", "str"]
    desc = "This is a description."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name == "str"
    assert result.is_generator is False
    assert result.description == desc

def test_build_meta_returns_without_type():
    args = ["returns"]
    desc = "This is a description."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name is None
    assert result.is_generator is False
    assert result.description == desc

def test_build_meta_returns_invalid_args():
    args = ["returns", "str", "extra"]
    desc = "This is a description."
    with pytest.raises(ParseError, match="Expected one or no arguments for a returns keyword."):
        _build_meta(args, desc)

def test_build_meta_raises_with_type():
    args = ["raises", "ValueError"]
    desc = "This is a description."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringRaises)
    assert result.type_name == "ValueError"
    assert result.description == desc

def test_build_meta_raises_without_type():
    args = ["raises"]
    desc = "This is a description."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringRaises)
    assert result.type_name is None
    assert result.description == desc

def test_build_meta_raises_invalid_args():
    args = ["raises", "ValueError", "extra"]
    desc = "This is a description."
    with pytest.raises(ParseError, match="Expected one or no arguments for a raises keyword."):
        _build_meta(args, desc)

def test_build_meta_generic():
    args = ["custom"]
    desc = "This is a description."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringMeta)
    assert result.args == args
    assert result.description == desc
