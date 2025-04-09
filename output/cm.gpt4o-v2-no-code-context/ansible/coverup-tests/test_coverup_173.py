# file: lib/ansible/module_utils/common/text/converters.py:286-302
# asked: {"lines": [286, 293, 294, 295, 296, 297, 298, 299, 300, 302], "branches": [[293, 294], [293, 295], [295, 296], [295, 297], [297, 298], [297, 299], [299, 300], [299, 302]]}
# gained: {"lines": [286, 293, 294, 295, 296, 297, 298, 299, 300, 302], "branches": [[293, 294], [293, 295], [295, 296], [295, 297], [297, 298], [297, 299], [299, 300], [299, 302]]}

import pytest
from ansible.module_utils.common.text.converters import container_to_bytes
from ansible.module_utils._text import to_bytes, text_type

def test_container_to_bytes_string():
    result = container_to_bytes("test string")
    assert result == to_bytes("test string")

def test_container_to_bytes_dict():
    result = container_to_bytes({"key": "value"})
    assert result == {to_bytes("key"): to_bytes("value")}

def test_container_to_bytes_list():
    result = container_to_bytes(["item1", "item2"])
    assert result == [to_bytes("item1"), to_bytes("item2")]

def test_container_to_bytes_tuple():
    result = container_to_bytes(("item1", "item2"))
    assert result == (to_bytes("item1"), to_bytes("item2"))

def test_container_to_bytes_other():
    result = container_to_bytes(12345)
    assert result == 12345
