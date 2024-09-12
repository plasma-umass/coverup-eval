# file: docstring_parser/common.py:24-42
# asked: {"lines": [24, 25, 33, 41, 42], "branches": []}
# gained: {"lines": [24, 25, 33, 41, 42], "branches": []}

import pytest
from docstring_parser.common import DocstringMeta

def test_docstring_meta_initialization():
    args = ["param1", "param2"]
    description = "This is a description."
    
    doc_meta = DocstringMeta(args, description)
    
    assert doc_meta.args == args
    assert doc_meta.description == description
