# file: tornado/escape.py:43-56
# asked: {"lines": [43, 54, 55], "branches": []}
# gained: {"lines": [43, 54, 55], "branches": []}

import pytest
from tornado.escape import xhtml_escape

def test_xhtml_escape():
    # Test with a string containing characters to be escaped
    input_str = 'Tom & Jerry < "Cartoon" >'
    expected_output = 'Tom &amp; Jerry &lt; &quot;Cartoon&quot; &gt;'
    assert xhtml_escape(input_str) == expected_output

    # Test with a string containing a single quote
    input_str = "It's a test"
    expected_output = "It&#39;s a test"
    assert xhtml_escape(input_str) == expected_output

    # Test with bytes input
    input_bytes = b'Tom & Jerry < "Cartoon" >'
    expected_output = 'Tom &amp; Jerry &lt; &quot;Cartoon&quot; &gt;'
    assert xhtml_escape(input_bytes) == expected_output

    # Test with an empty string
    input_str = ''
    expected_output = ''
    assert xhtml_escape(input_str) == expected_output

    # Test with a string with no characters to be escaped
    input_str = 'Hello World'
    expected_output = 'Hello World'
    assert xhtml_escape(input_str) == expected_output
