# file: lib/ansible/module_utils/common/text/converters.py:305-322
# asked: {"lines": [305, 312, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[312, 314], [312, 315], [315, 316], [315, 317], [317, 318], [317, 319], [319, 320], [319, 322]]}
# gained: {"lines": [305, 312, 314, 315, 316, 317, 318, 319, 320, 322], "branches": [[312, 314], [312, 315], [315, 316], [315, 317], [317, 318], [317, 319], [319, 320], [319, 322]]}

import pytest
from ansible.module_utils.common.text.converters import container_to_text
from ansible.module_utils.six import binary_type

def test_container_to_text_with_binary_type():
    binary_data = b"binary data"
    result = container_to_text(binary_data)
    assert result == "binary data"

def test_container_to_text_with_dict():
    data = {b"key": b"value"}
    result = container_to_text(data)
    assert result == {"key": "value"}

def test_container_to_text_with_list():
    data = [b"item1", b"item2"]
    result = container_to_text(data)
    assert result == ["item1", "item2"]

def test_container_to_text_with_tuple():
    data = (b"item1", b"item2")
    result = container_to_text(data)
    assert result == ("item1", "item2")

def test_container_to_text_with_other():
    data = 123
    result = container_to_text(data)
    assert result == 123
