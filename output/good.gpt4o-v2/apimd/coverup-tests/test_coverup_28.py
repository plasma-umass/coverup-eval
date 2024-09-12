# file: apimd/parser.py:90-98
# asked: {"lines": [94, 98], "branches": [[93, 94], [95, 98]]}
# gained: {"lines": [94, 98], "branches": [[93, 94], [95, 98]]}

import pytest
from apimd.parser import code

def test_code_with_ampersand():
    result = code("example & text")
    assert result == "<code>example & text</code>"

def test_code_with_non_empty_string():
    result = code("example text")
    assert result == "`example text`"

def test_code_with_empty_string():
    result = code("")
    assert result == " "
