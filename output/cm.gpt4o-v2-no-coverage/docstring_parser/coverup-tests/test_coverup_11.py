# file: docstring_parser/common.py:65-80
# asked: {"lines": [65, 66, 68, 74, 77, 78, 79, 80], "branches": []}
# gained: {"lines": [65, 66, 68, 74, 77, 78, 79, 80], "branches": []}

import pytest
from docstring_parser.common import DocstringReturns, DocstringMeta

def test_docstring_returns_init():
    args = ["arg1", "arg2"]
    description = "This is a description"
    type_name = "str"
    is_generator = True
    return_name = "result"

    docstring_returns = DocstringReturns(args, description, type_name, is_generator, return_name)

    assert docstring_returns.args == args
    assert docstring_returns.description == description
    assert docstring_returns.type_name == type_name
    assert docstring_returns.is_generator is True
    assert docstring_returns.return_name == return_name

def test_docstring_returns_init_no_return_name():
    args = ["arg1", "arg2"]
    description = "This is a description"
    type_name = "str"
    is_generator = False

    docstring_returns = DocstringReturns(args, description, type_name, is_generator)

    assert docstring_returns.args == args
    assert docstring_returns.description == description
    assert docstring_returns.type_name == type_name
    assert docstring_returns.is_generator is False
    assert docstring_returns.return_name is None
