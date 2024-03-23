# file flutils/strutils.py:47-72
# lines [68, 69, 70, 71, 72]
# branches ['70->71', '70->72']

import pytest
from flutils.strutils import as_escaped_utf8_literal

def test_as_escaped_utf8_literal_non_ascii():
    # Test with non-ASCII characters to ensure lines 68-72 are covered
    text = '1.★ 🛑'
    expected = '\\x31\\x2e\\xe2\\x98\\x85\\x20\\xf0\\x9f\\x9b\\x91'
    result = as_escaped_utf8_literal(text)
    assert result == expected, "The escaped UTF8 hexadecimal representation does not match the expected result."
