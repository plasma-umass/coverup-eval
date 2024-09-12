# file: lib/ansible/module_utils/common/text/converters.py:150-238
# asked: {"lines": [150, 201, 202, 204, 205, 206, 207, 208, 210, 212, 216, 220, 221, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 233, 234, 236, 238], "branches": [[201, 202], [201, 204], [204, 205], [204, 212], [205, 206], [205, 207], [207, 208], [207, 210], [212, 216], [212, 220], [220, 221], [220, 229], [229, 230], [229, 231], [231, 232], [231, 233], [233, 234], [233, 236]]}
# gained: {"lines": [150, 201, 202, 204, 205, 206, 212, 216, 220, 221, 222, 229, 230, 231, 232, 233, 234, 236, 238], "branches": [[201, 202], [201, 204], [204, 205], [205, 206], [212, 216], [212, 220], [220, 221], [220, 229], [229, 230], [229, 231], [231, 232], [231, 233], [233, 234], [233, 236]]}

import pytest
from ansible.module_utils.common.text.converters import to_text

def test_to_text_text_type():
    assert to_text("hello") == "hello"

def test_to_text_binary_type():
    assert to_text(b"hello") == "hello"

def test_to_text_binary_type_with_encoding():
    assert to_text(b"\xe4\xbd\xa0\xe5\xa5\xbd", encoding='utf-8') == "你好"

def test_to_text_surrogate_or_strict():
    assert to_text(b"\xe4\xbd\xa0\xe5\xa5\xbd", errors='surrogate_or_strict') == "你好"

def test_to_text_surrogate_or_replace():
    assert to_text(b"\xe4\xbd\xa0\xe5\xa5\xbd", errors='surrogate_or_replace') == "你好"

def test_to_text_surrogate_then_replace():
    assert to_text(b"\xe4\xbd\xa0\xe5\xa5\xbd", errors='surrogate_then_replace') == "你好"

def test_to_text_nonstring_simplerepr():
    class CustomObject:
        def __str__(self):
            return "custom object"
    assert to_text(CustomObject(), nonstring='simplerepr') == "custom object"

def test_to_text_nonstring_empty():
    class CustomObject:
        def __str__(self):
            return "custom object"
    assert to_text(CustomObject(), nonstring='empty') == ""

def test_to_text_nonstring_passthru():
    class CustomObject:
        def __str__(self):
            return "custom object"
    obj = CustomObject()
    assert to_text(obj, nonstring='passthru') is obj

def test_to_text_nonstring_strict():
    class CustomObject:
        def __str__(self):
            return "custom object"
    with pytest.raises(TypeError, match='obj must be a string type'):
        to_text(CustomObject(), nonstring='strict')

def test_to_text_invalid_nonstring():
    class CustomObject:
        def __str__(self):
            return "custom object"
    with pytest.raises(TypeError, match="Invalid value invalid for to_text's nonstring parameter"):
        to_text(CustomObject(), nonstring='invalid')
