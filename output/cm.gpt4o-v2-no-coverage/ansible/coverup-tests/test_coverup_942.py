# file: lib/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [145, 146], "branches": []}
# gained: {"lines": [145, 146], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import to_unsafe_text
from ansible.module_utils._text import to_text
from ansible.module_utils.six import text_type, binary_type

def test_to_unsafe_text_with_text_type():
    result = to_unsafe_text("test string")
    assert isinstance(result, text_type)
    assert result == "test string"

def test_to_unsafe_text_with_binary_type():
    result = to_unsafe_text(b"test string")
    assert isinstance(result, text_type)
    assert result == "test string"

def test_to_unsafe_text_with_nonstring_simplerepr():
    class TestClass:
        def __str__(self):
            return "test class"
    result = to_unsafe_text(TestClass())
    assert isinstance(result, text_type)
    assert result == "test class"

def test_to_unsafe_text_with_nonstring_empty():
    result = to_unsafe_text(123, nonstring='empty')
    assert isinstance(result, text_type)
    assert result == ""

def test_to_unsafe_text_with_nonstring_passthru():
    result = to_unsafe_text(123, nonstring='passthru')
    assert result == 123

def test_to_unsafe_text_with_nonstring_strict():
    with pytest.raises(TypeError):
        to_unsafe_text(123, nonstring='strict')

def test_to_unsafe_text_with_invalid_nonstring():
    with pytest.raises(TypeError):
        to_unsafe_text(123, nonstring='invalid')
