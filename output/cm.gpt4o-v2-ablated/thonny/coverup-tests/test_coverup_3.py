# file: thonny/jedi_utils.py:46-49
# asked: {"lines": [46, 47, 49], "branches": []}
# gained: {"lines": [46, 47, 49], "branches": []}

import pytest
import parso
from thonny.jedi_utils import parse_source

def test_parse_source_valid_code():
    source = "def foo():\n    return 42"
    tree = parse_source(source)
    assert tree is not None
    assert tree.type == 'file_input'

def test_parse_source_invalid_code():
    source = "def foo(:\n    return 42"
    tree = parse_source(source)
    assert tree is not None
    assert tree.type == 'file_input'

def test_parse_source_empty_code():
    source = ""
    tree = parse_source(source)
    assert tree is not None
    assert tree.type == 'file_input'
