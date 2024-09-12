# file: tornado/escape.py:43-56
# asked: {"lines": [43, 54, 55], "branches": []}
# gained: {"lines": [43, 54, 55], "branches": []}

import pytest
from tornado.escape import xhtml_escape

def test_xhtml_escape():
    # Test escaping of special characters
    assert xhtml_escape('<>&"\'' ) == '&lt;&gt;&amp;&quot;&#39;'
    assert xhtml_escape('Hello & Welcome') == 'Hello &amp; Welcome'
    assert xhtml_escape('5 > 3') == '5 &gt; 3'
    assert xhtml_escape('Use "quotes"') == 'Use &quot;quotes&quot;'
    assert xhtml_escape("It's a test") == 'It&#39;s a test'

    # Test with bytes input
    assert xhtml_escape(b'<>&"\'' ) == '&lt;&gt;&amp;&quot;&#39;'
    assert xhtml_escape(b'Hello & Welcome') == 'Hello &amp; Welcome'
    assert xhtml_escape(b'5 > 3') == '5 &gt; 3'
    assert xhtml_escape(b'Use "quotes"') == 'Use &quot;quotes&quot;'
    assert xhtml_escape(b"It's a test") == 'It&#39;s a test'
