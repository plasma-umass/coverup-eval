# file tornado/escape.py:111-115
# lines [111, 112, 113, 115]
# branches []

import pytest
from tornado.escape import url_unescape

def test_url_unescape():
    # Test with string input
    assert url_unescape('foo%20bar') == 'foo bar'
    assert url_unescape('foo%20bar', plus=False) == 'foo bar'
    assert url_unescape('foo+bar') == 'foo bar'
    assert url_unescape('foo+bar', plus=False) == 'foo+bar'

    # Test with bytes input
    assert url_unescape(b'foo%20bar') == 'foo bar'
    assert url_unescape(b'foo%20bar', plus=False) == 'foo bar'
    assert url_unescape(b'foo+bar') == 'foo bar'
    assert url_unescape(b'foo+bar', plus=False) == 'foo+bar'

    # Test with different encoding
    assert url_unescape('foo%20bar', encoding='ascii') == 'foo bar'

    # Test with invalid percent-encoding (should not raise an exception)
    assert url_unescape('foo%') == 'foo%'
    assert url_unescape('foo%2') == 'foo%2'
    assert url_unescape('foo%2X') == 'foo%2X'

    # Test with non-default encoding
    snowman_utf8 = '%E2%98%83'
    snowman_latin1 = '%83'
    assert url_unescape(snowman_utf8, encoding='utf-8') == '\u2603'
    assert url_unescape(snowman_latin1, encoding='latin1') == '\u0083'
