# file: isort/format.py:89-91
# asked: {"lines": [89, 90, 91], "branches": []}
# gained: {"lines": [89, 90, 91], "branches": []}

import pytest
from isort.format import remove_whitespace

def test_remove_whitespace():
    # Test with default line separator
    content = "Hello \n World \x0c"
    expected = "HelloWorld"
    assert remove_whitespace(content) == expected

    # Test with custom line separator
    content = "Hello | World \x0c"
    expected = "HelloWorld"
    assert remove_whitespace(content, line_separator="|") == expected

    # Test with no whitespace to remove
    content = "HelloWorld"
    expected = "HelloWorld"
    assert remove_whitespace(content) == expected

    # Test with only whitespace
    content = " \n \x0c "
    expected = ""
    assert remove_whitespace(content) == expected

    # Test with empty string
    content = ""
    expected = ""
    assert remove_whitespace(content) == expected
