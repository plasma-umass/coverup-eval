# file: tornado/escape.py:59-61
# asked: {"lines": [61], "branches": []}
# gained: {"lines": [61], "branches": []}

import pytest
from tornado.escape import xhtml_unescape

def test_xhtml_unescape():
    # Test numeric character reference
    assert xhtml_unescape("&#65;") == "A"
    assert xhtml_unescape("&#x41;") == "A"
    
    # Test named character reference
    assert xhtml_unescape("&amp;") == "&"
    
    # Test invalid numeric character reference
    assert xhtml_unescape("&#invalid;") == "&#invalid;"
    
    # Test invalid named character reference
    assert xhtml_unescape("&unknown;") == "&unknown;"
