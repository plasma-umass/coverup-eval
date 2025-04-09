# file: isort/format.py:89-91
# asked: {"lines": [89, 90, 91], "branches": []}
# gained: {"lines": [89, 90, 91], "branches": []}

import pytest
from isort.format import remove_whitespace

def test_remove_whitespace():
    # Test with default line_separator
    content = "This is a test\nwith multiple lines\nand some spaces."
    expected = "Thisisatestwithmultiplelinesandsomespaces."
    assert remove_whitespace(content) == expected

    # Test with custom line_separator
    content = "This is a test|with multiple lines|and some spaces."
    expected = "Thisisatestwithmultiplelinesandsomespaces."
    assert remove_whitespace(content, line_separator="|") == expected

    # Test with form feed character
    content = "This is a test\nwith multiple lines\nand some spaces.\x0c"
    expected = "Thisisatestwithmultiplelinesandsomespaces."
    assert remove_whitespace(content) == expected

    # Test with only whitespace characters
    content = " \n \x0c "
    expected = ""
    assert remove_whitespace(content) == expected
