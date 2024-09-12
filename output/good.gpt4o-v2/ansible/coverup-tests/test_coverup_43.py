# file: lib/ansible/module_utils/common/text/converters.py:150-238
# asked: {"lines": [150, 201, 202, 204, 205, 206, 207, 208, 210, 212, 216, 220, 221, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 233, 234, 236, 238], "branches": [[201, 202], [201, 204], [204, 205], [204, 212], [205, 206], [205, 207], [207, 208], [207, 210], [212, 216], [212, 220], [220, 221], [220, 229], [229, 230], [229, 231], [231, 232], [231, 233], [233, 234], [233, 236]]}
# gained: {"lines": [150, 201, 202, 204, 205, 206, 207, 210, 212, 216, 220, 221, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 233, 234, 236, 238], "branches": [[201, 202], [201, 204], [204, 205], [205, 206], [205, 207], [207, 210], [212, 216], [212, 220], [220, 221], [220, 229], [229, 230], [229, 231], [231, 232], [231, 233], [233, 234], [233, 236]]}

import pytest
from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils.six import binary_type, text_type

def test_to_text_with_text_type():
    assert to_text("hello") == "hello"

def test_to_text_with_binary_type():
    assert to_text(b"hello") == "hello"

def test_to_text_with_surrogateescape(monkeypatch):
    monkeypatch.setattr("ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE", True)
    assert to_text(b"\xed\xb9\x81", errors='surrogate_or_strict') == "\udced\udcb9\udc81"

def test_to_text_with_surrogate_or_strict():
    assert to_text(b"\xed\xb9\x81", errors='surrogate_or_strict') == "\udced\udcb9\udc81"

def test_to_text_with_surrogate_or_replace(monkeypatch):
    monkeypatch.setattr("ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE", False)
    assert to_text(b"\xed\xb9\x81", errors='surrogate_or_replace') == "\ufffd\ufffd\ufffd"

def test_to_text_with_surrogate_then_replace(monkeypatch):
    monkeypatch.setattr("ansible.module_utils.common.text.converters.HAS_SURROGATEESCAPE", False)
    assert to_text(b"\xed\xb9\x81", errors='surrogate_then_replace') == "\ufffd\ufffd\ufffd"

def test_to_text_with_nonstring_simplerepr():
    class TestClass:
        def __str__(self):
            return "test"
    assert to_text(TestClass(), nonstring='simplerepr') == "test"

def test_to_text_with_nonstring_empty():
    class TestClass:
        def __str__(self):
            return "test"
    assert to_text(TestClass(), nonstring='empty') == ""

def test_to_text_with_nonstring_passthru():
    class TestClass:
        def __str__(self):
            return "test"
    obj = TestClass()
    assert to_text(obj, nonstring='passthru') is obj

def test_to_text_with_nonstring_strict():
    class TestClass:
        def __str__(self):
            return "test"
    with pytest.raises(TypeError):
        to_text(TestClass(), nonstring='strict')

def test_to_text_with_invalid_nonstring():
    class TestClass:
        def __str__(self):
            return "test"
    with pytest.raises(TypeError):
        to_text(TestClass(), nonstring='invalid')

def test_to_text_with_unicode_error_in_str():
    class TestClass:
        def __str__(self):
            raise UnicodeError()
        def __repr__(self):
            return "test"
    assert to_text(TestClass(), nonstring='simplerepr') == "test"

def test_to_text_with_unicode_error_in_repr():
    class TestClass:
        def __str__(self):
            raise UnicodeError()
        def __repr__(self):
            raise UnicodeError()
    assert to_text(TestClass(), nonstring='simplerepr') == ""
