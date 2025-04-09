# file isort/format.py:89-91
# lines [89, 90, 91]
# branches []

import pytest
from isort.format import remove_whitespace

def test_remove_whitespace():
    # Test with default line_separator
    assert remove_whitespace("line 1\nline 2") == "line1line2"
    assert remove_whitespace("line 1 line 2") == "line1line2"
    assert remove_whitespace("line 1\x0cline 2") == "line1line2"

    # Test with custom line_separator
    assert remove_whitespace("line 1\r\nline 2", line_separator="\r\n") == "line1line2"
    assert remove_whitespace("line 1 line 2", line_separator="\r\n") == "line1line2"
    assert remove_whitespace("line 1\x0cline 2", line_separator="\r\n") == "line1line2"
