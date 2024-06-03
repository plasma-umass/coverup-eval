# file tornado/escape.py:43-56
# lines [43, 54, 55]
# branches []

import pytest
from tornado.escape import xhtml_escape

def test_xhtml_escape():
    # Test with a string containing characters that need to be escaped
    input_str = '<div class="test">Hello & Welcome!</div>'
    expected_output = '&lt;div class=&quot;test&quot;&gt;Hello &amp; Welcome!&lt;/div&gt;'
    assert xhtml_escape(input_str) == expected_output

    # Test with a string containing a single quote
    input_str = "It's a test"
    expected_output = 'It&#39;s a test'
    assert xhtml_escape(input_str) == expected_output

    # Test with a bytes input
    input_bytes = b'<div class="test">Hello & Welcome!</div>'
    expected_output = '&lt;div class=&quot;test&quot;&gt;Hello &amp; Welcome!&lt;/div&gt;'
    assert xhtml_escape(input_bytes) == expected_output

    # Test with an empty string
    input_str = ''
    expected_output = ''
    assert xhtml_escape(input_str) == expected_output

    # Test with a string that does not need escaping
    input_str = 'Hello World'
    expected_output = 'Hello World'
    assert xhtml_escape(input_str) == expected_output
