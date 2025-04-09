# file: isort/format.py:89-91
# asked: {"lines": [89, 90, 91], "branches": []}
# gained: {"lines": [89, 90, 91], "branches": []}

import pytest
from isort.format import remove_whitespace

def test_remove_whitespace_default_separator():
    content = "This is a test\nwith multiple\nlines."
    expected = "Thisisatestwithmultiplelines."
    result = remove_whitespace(content)
    assert result == expected

def test_remove_whitespace_custom_separator():
    content = "This is a test|with multiple|lines."
    expected = "Thisisatestwithmultiplelines."
    result = remove_whitespace(content, line_separator="|")
    assert result == expected

def test_remove_whitespace_with_form_feed():
    content = "This is a test\nwith multiple\nlines.\x0c"
    expected = "Thisisatestwithmultiplelines."
    result = remove_whitespace(content)
    assert result == expected
