# file isort/format.py:89-91
# lines [89, 90, 91]
# branches []

import pytest
from isort.format import remove_whitespace

def test_remove_whitespace():
    # Test with default line separator
    content = "This is a test\nwith multiple lines\nand spaces."
    expected = "Thisisatestwithmultiplelinesandspaces."
    assert remove_whitespace(content) == expected

    # Test with custom line separator
    content = "This is a test\rwith multiple lines\r and spaces."
    expected = "Thisisatestwithmultiplelinesandspaces."
    assert remove_whitespace(content, line_separator="\r") == expected

    # Test with form feed character
    content = "This is a test\x0cwith form feed\x0c and spaces."
    expected = "Thisisatestwithformfeedandspaces."
    assert remove_whitespace(content) == expected

    # Test with empty content
    content = ""
    expected = ""
    assert remove_whitespace(content) == expected

    # Test with content that has no whitespace
    content = "NoWhitespaceHere"
    expected = "NoWhitespaceHere"
    assert remove_whitespace(content) == expected
