# file: docstring_parser/common.py:45-62
# asked: {"lines": [45, 46, 48, 58, 59, 60, 61, 62], "branches": []}
# gained: {"lines": [45, 46, 48, 58, 59, 60, 61, 62], "branches": []}

import pytest
from docstring_parser.common import DocstringParam

def test_docstring_param_initialization():
    args = ["arg1", "arg2"]
    description = "This is a description"
    arg_name = "param_name"
    type_name = "str"
    is_optional = True
    default = "default_value"

    param = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    assert param.args == args
    assert param.description == description
    assert param.arg_name == arg_name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default
