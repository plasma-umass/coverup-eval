# file: docstring_parser/common.py:45-62
# asked: {"lines": [45, 46, 48, 58, 59, 60, 61, 62], "branches": []}
# gained: {"lines": [45, 46, 48, 58, 59, 60, 61, 62], "branches": []}

import pytest
from docstring_parser.common import DocstringParam, DocstringMeta

def test_docstring_param_init():
    args = ["arg1", "arg2"]
    description = "This is a description"
    arg_name = "param1"
    type_name = "str"
    is_optional = True
    default = "default_value"

    docstring_param = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    assert docstring_param.args == args
    assert docstring_param.description == description
    assert docstring_param.arg_name == arg_name
    assert docstring_param.type_name == type_name
    assert docstring_param.is_optional == is_optional
    assert docstring_param.default == default

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: nothing to setup before each test
    yield
    # Teardown: nothing to teardown after each test
