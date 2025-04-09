# file: tornado/auth.py:1170-1173
# asked: {"lines": [1171, 1172, 1173], "branches": [[1171, 1172], [1171, 1173]]}
# gained: {"lines": [1171, 1172, 1173], "branches": [[1171, 1172], [1171, 1173]]}

import pytest
import urllib.parse
from tornado.util import unicode_type
from tornado.auth import _oauth_escape

def test_oauth_escape_with_str():
    input_val = "test_string"
    expected_output = urllib.parse.quote(input_val, safe="~")
    assert _oauth_escape(input_val) == expected_output

def test_oauth_escape_with_unicode():
    input_val = unicode_type("test_unicode")
    expected_output = urllib.parse.quote(input_val.encode("utf-8"), safe="~")
    assert _oauth_escape(input_val) == expected_output

def test_oauth_escape_with_bytes():
    input_val = b"test_bytes"
    expected_output = urllib.parse.quote(input_val, safe="~")
    assert _oauth_escape(input_val) == expected_output
