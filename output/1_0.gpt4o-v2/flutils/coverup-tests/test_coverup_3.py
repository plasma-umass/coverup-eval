# file: flutils/strutils.py:47-72
# asked: {"lines": [47, 68, 69, 70, 71, 72], "branches": [[70, 71], [70, 72]]}
# gained: {"lines": [47, 68, 69, 70, 71, 72], "branches": [[70, 71], [70, 72]]}

import pytest
from flutils.strutils import as_escaped_utf8_literal

def test_as_escaped_utf8_literal():
    # Test with a simple string
    assert as_escaped_utf8_literal('abc') == '\\x61\\x62\\x63'
    
    # Test with a string containing special characters
    assert as_escaped_utf8_literal('1.★ 🛑') == '\\x31\\x2e\\xe2\\x98\\x85\\x20\\xf0\\x9f\\x9b\\x91'
    
    # Test with an empty string
    assert as_escaped_utf8_literal('') == ''
    
    # Test with a string containing non-ASCII characters
    assert as_escaped_utf8_literal('你好') == '\\xe4\\xbd\\xa0\\xe5\\xa5\\xbd'
