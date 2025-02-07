# file: lib/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [145, 146], "branches": []}
# gained: {"lines": [145, 146], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import to_unsafe_text
from ansible.module_utils._text import to_text
from ansible.utils.unsafe_proxy import wrap_var

def test_to_unsafe_text_with_string():
    result = to_unsafe_text("test string")
    assert result == wrap_var(to_text("test string"))

def test_to_unsafe_text_with_bytes():
    result = to_unsafe_text(b"test bytes")
    assert result == wrap_var(to_text(b"test bytes"))

def test_to_unsafe_text_with_nonstring():
    result = to_unsafe_text(12345)
    assert result == wrap_var(to_text(12345))

def test_to_unsafe_text_with_kwargs():
    result = to_unsafe_text("test string", encoding='utf-8', errors='strict')
    assert result == wrap_var(to_text("test string", encoding='utf-8', errors='strict'))
