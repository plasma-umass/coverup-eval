# file docstring_parser/common.py:83-95
# lines [83, 84, 86, 93, 94, 95]
# branches []

import pytest
from docstring_parser.common import DocstringRaises

def test_docstring_raises_initialization():
    args = ["arg1", "arg2"]
    description = "This is a description"
    type_name = "TypeName"

    docstring_raises = DocstringRaises(args, description, type_name)

    assert docstring_raises.args == args
    assert docstring_raises.description == description
    assert docstring_raises.type_name == type_name

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
