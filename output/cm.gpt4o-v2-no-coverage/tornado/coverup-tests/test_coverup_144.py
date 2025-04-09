# file: tornado/escape.py:59-61
# asked: {"lines": [59, 61], "branches": []}
# gained: {"lines": [59, 61], "branches": []}

import pytest
from tornado.escape import xhtml_unescape

def test_xhtml_unescape():
    # Test with named entity
    assert xhtml_unescape("&lt;") == "<"
    # Test with numeric entity
    assert xhtml_unescape("&#60;") == "<"
    # Test with hexadecimal entity
    assert xhtml_unescape("&#x3c;") == "<"
    # Test with unknown entity
    assert xhtml_unescape("&unknown;") == "&unknown;"
    # Test with mixed content
    assert xhtml_unescape("Hello &lt;world&gt; &#33;") == "Hello <world> !"
    # Test with bytes input
    assert xhtml_unescape(b"&lt;") == "<"
