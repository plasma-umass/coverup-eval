# file: docstring_parser/rest.py:21-83
# asked: {"lines": [21, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 41, 42, 44, 45, 46, 47, 48, 49, 50, 53, 54, 55, 56, 57, 59, 60, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 76, 77, 79, 80, 83], "branches": [[24, 25], [24, 53], [25, 26], [25, 32], [27, 28], [27, 31], [32, 33], [32, 37], [53, 54], [53, 70], [54, 55], [54, 56], [56, 57], [56, 59], [70, 71], [70, 83], [71, 72], [71, 73], [73, 74], [73, 76]]}
# gained: {"lines": [21], "branches": []}

import pytest
from docstring_parser.common import DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises, ParseError
import re

PARAM_KEYWORDS = {"param", "parameter", "arg", "argument"}
RETURNS_KEYWORDS = {"returns", "return"}
YIELDS_KEYWORDS = {"yields", "yield"}
RAISES_KEYWORDS = {"raises", "raise"}

def _build_meta(args, desc):
    key = args[0]

    if key in PARAM_KEYWORDS:
        if len(args) == 3:
            key, type_name, arg_name = args
            if type_name.endswith("?"):
                is_optional = True
                type_name = type_name[:-1]
            else:
                is_optional = False
        elif len(args) == 2:
            key, arg_name = args
            type_name = None
            is_optional = None
        else:
            raise ParseError(
                "Expected one or two arguments for a {} keyword.".format(key)
            )

        m = re.match(r".*defaults to (.+)", desc, flags=re.DOTALL)
        default = m.group(1).rstrip(".") if m else None

        return DocstringParam(
            args=args,
            description=desc,
            arg_name=arg_name,
            type_name=type_name,
            is_optional=is_optional,
            default=default,
        )

    if key in RETURNS_KEYWORDS | YIELDS_KEYWORDS:
        if len(args) == 2:
            type_name = args[1]
        elif len(args) == 1:
            type_name = None
        else:
            raise ParseError(
                "Expected one or no arguments for a {} keyword.".format(key)
            )

        return DocstringReturns(
            args=args,
            description=desc,
            type_name=type_name,
            is_generator=key in YIELDS_KEYWORDS,
        )

    if key in RAISES_KEYWORDS:
        if len(args) == 2:
            type_name = args[1]
        elif len(args) == 1:
            type_name = None
        else:
            raise ParseError(
                "Expected one or no arguments for a {} keyword.".format(key)
            )
        return DocstringRaises(
            args=args, description=desc, type_name=type_name
        )

    return DocstringMeta(args=args, description=desc)

def test_build_meta_param_with_type_and_optional():
    args = ["param", "int?", "x"]
    desc = "An integer parameter. defaults to 10."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "x"
    assert result.type_name == "int"
    assert result.is_optional is True
    assert result.default == "10"

def test_build_meta_param_with_type():
    args = ["param", "int", "x"]
    desc = "An integer parameter."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "x"
    assert result.type_name == "int"
    assert result.is_optional is False
    assert result.default is None

def test_build_meta_param_without_type():
    args = ["param", "x"]
    desc = "A parameter."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.arg_name == "x"
    assert result.type_name is None
    assert result.is_optional is None
    assert result.default is None

def test_build_meta_param_invalid_args():
    args = ["param"]
    desc = "A parameter."
    with pytest.raises(ParseError):
        _build_meta(args, desc)

def test_build_meta_returns_with_type():
    args = ["returns", "int"]
    desc = "Returns an integer."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name == "int"
    assert result.is_generator is False

def test_build_meta_returns_without_type():
    args = ["returns"]
    desc = "Returns a value."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name is None
    assert result.is_generator is False

def test_build_meta_yields_with_type():
    args = ["yields", "int"]
    desc = "Yields an integer."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name == "int"
    assert result.is_generator is True

def test_build_meta_yields_without_type():
    args = ["yields"]
    desc = "Yields a value."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringReturns)
    assert result.type_name is None
    assert result.is_generator is True

def test_build_meta_raises_with_type():
    args = ["raises", "ValueError"]
    desc = "Raises a ValueError."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringRaises)
    assert result.type_name == "ValueError"

def test_build_meta_raises_without_type():
    args = ["raises"]
    desc = "Raises an error."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringRaises)
    assert result.type_name is None

def test_build_meta_raises_invalid_args():
    args = ["raises", "ValueError", "extra"]
    desc = "Raises a ValueError."
    with pytest.raises(ParseError):
        _build_meta(args, desc)

def test_build_meta_unknown_key():
    args = ["unknown"]
    desc = "An unknown key."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringMeta)
    assert result.args == args
    assert result.description == desc
