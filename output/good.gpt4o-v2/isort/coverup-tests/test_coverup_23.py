# file: isort/format.py:89-91
# asked: {"lines": [89, 90, 91], "branches": []}
# gained: {"lines": [89, 90, 91], "branches": []}

import pytest
from isort.format import remove_whitespace

def test_remove_whitespace():
    # Test with default line separator
    content = "This is a test\nwith multiple lines\nand some spaces."
    expected = "Thisisatestwithmultiplelinesandsomespaces."
    assert remove_whitespace(content) == expected

    # Test with custom line separator
    content = "This is a test\r\nwith multiple lines\r\nand some spaces."
    expected = "Thisisatestwithmultiplelinesandsomespaces."
    assert remove_whitespace(content, line_separator="\r\n") == expected

    # Test with form feed character
    content = "This is a test\x0cwith a form feed."
    expected = "Thisisatestwithaformfeed."
    assert remove_whitespace(content) == expected

    # Test with spaces only
    content = "     "
    expected = ""
    assert remove_whitespace(content) == expected

    # Test with line separators only
    content = "\n\n\n"
    expected = ""
    assert remove_whitespace(content) == expected

    # Test with mixed whitespace characters
    content = " \n \x0c "
    expected = ""
    assert remove_whitespace(content) == expected
