# file: tornado/escape.py:43-56
# asked: {"lines": [43, 54, 55], "branches": []}
# gained: {"lines": [43, 54, 55], "branches": []}

import pytest
from tornado.escape import xhtml_escape

def test_xhtml_escape_string():
    assert xhtml_escape("<>&\"'") == "&lt;&gt;&amp;&quot;&#39;"

def test_xhtml_escape_bytes():
    assert xhtml_escape(b"<>&\"'") == "&lt;&gt;&amp;&quot;&#39;"

def test_xhtml_escape_mixed():
    assert xhtml_escape("Hello <>&\"' World") == "Hello &lt;&gt;&amp;&quot;&#39; World"

def test_xhtml_escape_no_special_chars():
    assert xhtml_escape("Hello World") == "Hello World"

def test_xhtml_escape_empty_string():
    assert xhtml_escape("") == ""

def test_xhtml_escape_empty_bytes():
    assert xhtml_escape(b"") == ""
