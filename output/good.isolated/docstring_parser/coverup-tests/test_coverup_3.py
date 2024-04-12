# file docstring_parser/common.py:24-42
# lines [24, 25, 33, 41, 42]
# branches []

import pytest
from docstring_parser.common import DocstringMeta

def test_docstring_meta_initialization():
    args = ["arg1", "arg2"]
    description = "Test description"
    meta = DocstringMeta(args, description)
    
    assert meta.args == args
    assert meta.description == description
