# file docstring_parser/common.py:65-80
# lines [65, 66, 68, 74, 77, 78, 79, 80]
# branches []

import pytest
from docstring_parser.common import DocstringReturns

def test_docstring_returns_init():
    args = ["arg1", "arg2"]
    description = "Some description"
    type_name = "SomeType"
    is_generator = True
    return_name = "return_value"

    # Test initialization with all parameters
    returns = DocstringReturns(
        args=args,
        description=description,
        type_name=type_name,
        is_generator=is_generator,
        return_name=return_name
    )

    assert returns.args == args
    assert returns.description == description
    assert returns.type_name == type_name
    assert returns.is_generator == is_generator
    assert returns.return_name == return_name

    # Test initialization with minimum parameters
    returns_min = DocstringReturns(
        args=args,
        description=description,
        type_name=type_name,
        is_generator=is_generator
    )

    assert returns_min.args == args
    assert returns_min.description == description
    assert returns_min.type_name == type_name
    assert returns_min.is_generator == is_generator
    assert returns_min.return_name is None
