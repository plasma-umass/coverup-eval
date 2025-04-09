# file: apimd/parser.py:90-98
# asked: {"lines": [90, 92, 93, 94, 95, 96, 98], "branches": [[93, 94], [93, 95], [95, 96], [95, 98]]}
# gained: {"lines": [90, 92, 93, 94, 95, 96, 98], "branches": [[93, 94], [93, 95], [95, 96], [95, 98]]}

import pytest
from apimd.parser import code

def test_code_with_pipe():
    assert code("example|text") == "<code>example&#124;text</code>"

def test_code_with_ampersand():
    assert code("example&text") == "<code>example&text</code>"

def test_code_with_text():
    assert code("example text") == "`example text`"

def test_code_with_empty_string():
    assert code("") == " "
