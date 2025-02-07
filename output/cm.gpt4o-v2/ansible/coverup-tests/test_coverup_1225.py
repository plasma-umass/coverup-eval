# file: lib/ansible/module_utils/common/text/converters.py:270-283
# asked: {"lines": [278, 279, 281, 282, 283], "branches": [[271, 283]]}
# gained: {"lines": [278, 279, 283], "branches": [[271, 283]]}

import pytest
from ansible.module_utils.common.text.converters import jsonify

def test_jsonify_utf8_encoding():
    data = {"key": "value"}
    result = jsonify(data)
    assert result == '{"key": "value"}'

def test_jsonify_latin1_encoding():
    data = {"key": "value".encode("latin-1")}
    result = jsonify(data)
    assert result == '{"key": "value"}'

def test_jsonify_type_error():
    data = {"key": set([1, 2, 3])}
    result = jsonify(data)
    assert result == '{"key": [1, 2, 3]}'

def test_jsonify_unicode_decode_error(mocker):
    mocker.patch('ansible.module_utils.common.text.converters.container_to_text', side_effect=UnicodeDecodeError("codec", b"", 0, 1, "reason"))
    data = {"key": b"\x80abc"}
    with pytest.raises(UnicodeError):
        jsonify(data)
