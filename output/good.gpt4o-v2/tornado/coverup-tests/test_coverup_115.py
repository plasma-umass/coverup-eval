# file: tornado/escape.py:106-108
# asked: {"lines": [106, 107, 108], "branches": []}
# gained: {"lines": [106, 107], "branches": []}

import pytest
from tornado.escape import url_unescape

def test_url_unescape_bytes_overload():
    # This test is to ensure the overload for bytes is covered
    result = url_unescape(b'%2F', encoding=None, plus=True)
    assert result == b'/'

def test_url_unescape_str_overload():
    # This test is to ensure the overload for str is covered
    result = url_unescape('%2F', encoding=None, plus=True)
    assert result == b'/'
