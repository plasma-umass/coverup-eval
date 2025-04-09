# file tornado/escape.py:43-56
# lines [43, 54, 55]
# branches []

import pytest
from tornado.escape import xhtml_escape

@pytest.fixture
def cleanup():
    # Fixture for any required cleanup, add if necessary
    yield
    # Cleanup code goes here if needed

def test_xhtml_escape(cleanup):
    # Test the xhtml_escape function for different characters
    assert xhtml_escape("<") == "&lt;"
    assert xhtml_escape(">") == "&gt;"
    assert xhtml_escape('"') == "&quot;"
    assert xhtml_escape("'") == "&#39;"
    assert xhtml_escape("&") == "&amp;"

    # Test with a combination of characters
    assert xhtml_escape("<div title='test & \"escaping\"'>") == \
           "&lt;div title=&#39;test &amp; &quot;escaping&quot;&#39;&gt;"

    # Test with non-string input that can be converted to string
    assert xhtml_escape(str(42)) == "42"
    assert xhtml_escape(str(None)) == "None"

    # Ensure the cleanup fixture is used
    cleanup
