# file docstring_parser/common.py:65-80
# lines [65, 66, 68, 74, 77, 78, 79, 80]
# branches []

import pytest
from docstring_parser.common import DocstringReturns

def test_docstring_returns_initialization():
    args = ["arg1", "arg2"]
    description = "This is a description."
    type_name = "str"
    is_generator = True
    return_name = "return_value"

    docstring_returns = DocstringReturns(
        args=args,
        description=description,
        type_name=type_name,
        is_generator=is_generator,
        return_name=return_name
    )

    assert docstring_returns.args == args
    assert docstring_returns.description == description
    assert docstring_returns.type_name == type_name
    assert docstring_returns.is_generator == is_generator
    assert docstring_returns.return_name == return_name
