# file: tornado/auth.py:1170-1173
# asked: {"lines": [1170, 1171, 1172, 1173], "branches": [[1171, 1172], [1171, 1173]]}
# gained: {"lines": [1170, 1171, 1172, 1173], "branches": [[1171, 1172], [1171, 1173]]}

import pytest
from tornado.auth import _oauth_escape
from tornado.util import unicode_type

def test_oauth_escape_with_unicode():
    input_val = "test_string"
    expected_output = "test_string"
    assert _oauth_escape(input_val) == expected_output

def test_oauth_escape_with_bytes():
    input_val = b"test_string"
    expected_output = "test_string"
    assert _oauth_escape(input_val) == expected_output

def test_oauth_escape_with_special_chars():
    input_val = "test string/with special&chars"
    expected_output = "test%20string%2Fwith%20special%26chars"
    assert _oauth_escape(input_val) == expected_output
