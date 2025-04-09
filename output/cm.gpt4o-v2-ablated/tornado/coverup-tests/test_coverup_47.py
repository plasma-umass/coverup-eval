# file: tornado/auth.py:1170-1173
# asked: {"lines": [1170, 1171, 1172, 1173], "branches": [[1171, 1172], [1171, 1173]]}
# gained: {"lines": [1170, 1171, 1172, 1173], "branches": [[1171, 1172], [1171, 1173]]}

import pytest
from tornado.auth import _oauth_escape
import urllib

def test_oauth_escape_with_unicode(monkeypatch):
    # Mock unicode_type to be str for Python 3 compatibility
    monkeypatch.setattr('tornado.auth.unicode_type', str)
    
    input_val = "test_string"
    expected_output = urllib.parse.quote(input_val.encode("utf-8"), safe="~")
    
    assert _oauth_escape(input_val) == expected_output

def test_oauth_escape_with_bytes():
    input_val = b"test_string"
    expected_output = urllib.parse.quote(input_val, safe="~")
    
    assert _oauth_escape(input_val) == expected_output

def test_oauth_escape_with_non_unicode():
    input_val = "test_string"
    expected_output = urllib.parse.quote(input_val, safe="~")
    
    assert _oauth_escape(input_val) == expected_output
