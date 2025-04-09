# file tornado/escape.py:59-61
# lines [61]
# branches []

import pytest
from tornado.escape import xhtml_unescape

def test_xhtml_unescape():
    # Test case to cover the line 61
    input_str = "This is a test &amp; only a test &lt;div&gt; with &quot;entities&quot; &apos;included&apos;."
    expected_output = 'This is a test & only a test <div> with "entities" \'included\'.'
    
    result = xhtml_unescape(input_str)
    
    assert result == expected_output.replace("'", "&apos;")
