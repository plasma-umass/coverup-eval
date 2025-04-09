# file: tornado/escape.py:43-56
# asked: {"lines": [43, 54, 55], "branches": []}
# gained: {"lines": [43, 54, 55], "branches": []}

import pytest
from tornado.escape import xhtml_escape

def test_xhtml_escape():
    # Test escaping of special characters
    assert xhtml_escape("<>&\"'") == "&lt;&gt;&amp;&quot;&#39;"
    
    # Test escaping of a string without special characters
    assert xhtml_escape("hello") == "hello"
    
    # Test escaping of bytes input
    assert xhtml_escape(b"<>&\"'") == "&lt;&gt;&amp;&quot;&#39;"
    
    # Test escaping of bytes input without special characters
    assert xhtml_escape(b"hello") == "hello"
