# file: lib/ansible/module_utils/common/text/converters.py:286-302
# asked: {"lines": [286, 293, 294, 295, 296, 297, 298, 299, 300, 302], "branches": [[293, 294], [293, 295], [295, 296], [295, 297], [297, 298], [297, 299], [299, 300], [299, 302]]}
# gained: {"lines": [286, 293, 294, 295, 296, 297, 298, 299, 300, 302], "branches": [[293, 294], [293, 295], [295, 296], [295, 297], [297, 298], [297, 299], [299, 300], [299, 302]]}

import pytest
from ansible.module_utils.common.text.converters import container_to_bytes
from ansible.module_utils.six import text_type

def test_container_to_bytes_with_text_type():
    result = container_to_bytes(text_type("test"))
    assert isinstance(result, bytes)
    assert result == b"test"

def test_container_to_bytes_with_dict():
    result = container_to_bytes({"key": "value"})
    assert isinstance(result, dict)
    assert result == {b"key": b"value"}

def test_container_to_bytes_with_list():
    result = container_to_bytes(["value1", "value2"])
    assert isinstance(result, list)
    assert result == [b"value1", b"value2"]

def test_container_to_bytes_with_tuple():
    result = container_to_bytes(("value1", "value2"))
    assert isinstance(result, tuple)
    assert result == (b"value1", b"value2")

def test_container_to_bytes_with_other():
    result = container_to_bytes(123)
    assert isinstance(result, int)
    assert result == 123
