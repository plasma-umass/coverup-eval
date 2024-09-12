# file: tornado/escape.py:43-56
# asked: {"lines": [43, 54, 55], "branches": []}
# gained: {"lines": [43, 54, 55], "branches": []}

import pytest
from tornado.escape import xhtml_escape

def test_xhtml_escape():
    # Test escaping of special characters
    assert xhtml_escape('<>&"\'') == '&lt;&gt;&amp;&quot;&#39;'
    
    # Test with a string that has no special characters
    assert xhtml_escape('hello') == 'hello'
    
    # Test with a string that has mixed content
    assert xhtml_escape('hello <world> & "everyone"') == 'hello &lt;world&gt; &amp; &quot;everyone&quot;'
    
    # Test with bytes input
    assert xhtml_escape(b'hello <world> & "everyone"') == 'hello &lt;world&gt; &amp; &quot;everyone&quot;'
    
    # Test with an empty string
    assert xhtml_escape('') == ''
    
    # Test with an empty bytes
    assert xhtml_escape(b'') == ''
