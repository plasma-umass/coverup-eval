# file: tornado/escape.py:59-61
# asked: {"lines": [59, 61], "branches": []}
# gained: {"lines": [59, 61], "branches": []}

import pytest
from tornado.escape import xhtml_unescape

def test_xhtml_unescape():
    # Test with a string containing an XML entity
    assert xhtml_unescape("Hello &amp; World") == "Hello & World"
    
    # Test with a string containing a numeric character reference
    assert xhtml_unescape("&#65;") == "A"
    
    # Test with a string containing a hexadecimal numeric character reference
    assert xhtml_unescape("&#x41;") == "A"
    
    # Test with a string containing an unknown entity
    assert xhtml_unescape("Hello &unknown; World") == "Hello &unknown; World"
    
    # Test with a bytes input
    assert xhtml_unescape(b"Hello &amp; World") == "Hello & World"
