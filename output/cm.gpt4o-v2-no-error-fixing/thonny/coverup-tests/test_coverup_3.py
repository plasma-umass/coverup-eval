# file: thonny/jedi_utils.py:46-49
# asked: {"lines": [46, 47, 49], "branches": []}
# gained: {"lines": [46, 47, 49], "branches": []}

import pytest
import parso
from thonny.jedi_utils import parse_source

def test_parse_source():
    source_code = "def foo():\n    return 42"
    parsed = parse_source(source_code)
    assert parsed is not None
    assert parsed.type == 'file_input'
    assert parsed.children[0].type == 'funcdef'
    assert parsed.children[0].name.value == 'foo'
