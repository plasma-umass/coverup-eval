# file docstring_parser/common.py:45-62
# lines [45, 46, 48, 58, 59, 60, 61, 62]
# branches []

import pytest
from docstring_parser.common import DocstringParam

def test_docstring_param_initialization():
    args = ["arg1", "arg2"]
    description = "A parameter description"
    arg_name = "param_name"
    type_name = "str"
    is_optional = True
    default = "None"

    param = DocstringParam(
        args=args,
        description=description,
        arg_name=arg_name,
        type_name=type_name,
        is_optional=is_optional,
        default=default
    )

    assert param.args == args
    assert param.description == description
    assert param.arg_name == arg_name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default
