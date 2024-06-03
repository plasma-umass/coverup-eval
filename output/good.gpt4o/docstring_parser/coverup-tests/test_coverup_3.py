# file docstring_parser/common.py:24-42
# lines [24, 25, 33, 41, 42]
# branches []

import pytest
from docstring_parser.common import DocstringMeta

def test_docstring_meta_initialization():
    # Test initialization with sample data
    args = ["arg1", "arg2"]
    description = "This is a description."
    meta = DocstringMeta(args, description)
    
    # Assertions to verify the postconditions
    assert meta.args == args
    assert meta.description == description

# Ensure the test is cleaned up properly
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
