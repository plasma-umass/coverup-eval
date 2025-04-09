# file: apimd/parser.py:90-98
# asked: {"lines": [90, 92, 93, 94, 95, 96, 98], "branches": [[93, 94], [93, 95], [95, 96], [95, 98]]}
# gained: {"lines": [90, 92, 93, 94, 95, 96, 98], "branches": [[93, 94], [93, 95], [95, 96], [95, 98]]}

import pytest

from apimd.parser import code

def test_code_with_pipe():
    assert code("a|b") == "<code>a&#124;b</code>"

def test_code_with_ampersand():
    assert code("a&b") == "<code>a&b</code>"

def test_code_with_other_chars():
    assert code("abc") == "`abc`"

def test_code_with_empty_string():
    assert code("") == " "
