# file apimd/parser.py:90-98
# lines [90, 92, 93, 94, 95, 96, 98]
# branches ['93->94', '93->95', '95->96', '95->98']

import pytest
from apimd.parser import code

def test_code_escapes_pipe():
    assert code("a|b") == "<code>a&#124;b</code>"

def test_code_contains_ampersand():
    assert code("a&b") == "<code>a&b</code>"

def test_code_non_empty_no_ampersand():
    assert code("abc") == "`abc`"

def test_code_empty_string():
    assert code("") == " "
