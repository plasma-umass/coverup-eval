# file: lib/ansible/galaxy/api.py:180-181
# asked: {"lines": [180, 181], "branches": []}
# gained: {"lines": [180, 181], "branches": []}

import pytest
from ansible.galaxy.api import _urljoin
from ansible.module_utils._text import to_native

def test_urljoin_basic():
    assert _urljoin('http://example.com', 'a', 'b/c') == 'http://example.com/a/b/c'

def test_urljoin_with_trailing_slash():
    assert _urljoin('http://example.com/', '/a/', 'b/c/') == 'http://example.com/a/b/c'

def test_urljoin_with_empty_string():
    assert _urljoin('http://example.com', '', 'a', '', 'b/c') == 'http://example.com/a/b/c'

def test_urljoin_with_none():
    assert _urljoin('http://example.com', None, 'a', None, 'b/c') == 'http://example.com/a/b/c'

def test_urljoin_with_special_characters():
    assert _urljoin('http://example.com', 'a b', 'c/d') == 'http://example.com/a b/c/d'

def test_to_native_with_surrogate_or_strict():
    assert to_native(b'\xe2\x98\x83', errors='surrogate_or_strict') == '☃'

def test_to_native_with_surrogate_or_replace():
    assert to_native(b'\xe2\x98\x83', errors='surrogate_or_replace') == '☃'

def test_to_native_with_surrogate_then_replace():
    assert to_native(b'\xe2\x98\x83', errors='surrogate_then_replace') == '☃'

def test_to_native_with_invalid_bytes():
    assert to_native(b'\xff', errors='replace') == '\ufffd'

def test_to_native_with_nonstring():
    assert to_native(123, nonstring='simplerepr') == '123'
