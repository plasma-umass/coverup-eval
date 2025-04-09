# file: lib/ansible/plugins/filter/core.py:460-461
# asked: {"lines": [460, 461], "branches": []}
# gained: {"lines": [460, 461], "branches": []}

import pytest
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.filter.core import b64encode

def test_b64encode_utf8():
    assert b64encode("hello") == "aGVsbG8="

def test_b64encode_different_encoding():
    assert b64encode("你好", encoding='utf-8') == "5L2g5aW9"

def test_b64encode_empty_string():
    assert b64encode("") == ""

def test_b64encode_special_characters():
    assert b64encode("!@#$%^&*()") == "IUAjJCVeJiooKQ=="

def test_b64encode_surrogate():
    with pytest.raises(UnicodeEncodeError):
        b64encode("hello\udc00world", encoding='ascii')
