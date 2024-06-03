# file lib/ansible/module_utils/common/text/converters.py:270-283
# lines [278, 279, 281, 282, 283]
# branches ['271->283']

import pytest
import json
from ansible.module_utils.common.text.converters import jsonify

def _json_encode_fallback(obj):
    return str(obj)

def container_to_text(data, encoding):
    if isinstance(data, bytes):
        return data.decode(encoding)
    elif isinstance(data, dict):
        return {container_to_text(k, encoding): container_to_text(v, encoding) for k, v in data.items()}
    elif isinstance(data, list):
        return [container_to_text(i, encoding) for i in data]
    return data

def test_jsonify_unicode_decode_error(mocker):
    # Mock container_to_text to raise UnicodeDecodeError
    mocker.patch('ansible.module_utils.common.text.converters.container_to_text', side_effect=UnicodeDecodeError("codec", b"", 0, 1, "reason"))

    data = {"key": b"\x80"}  # Invalid byte sequence for utf-8 and latin-1

    with pytest.raises(UnicodeError, match='Invalid unicode encoding encountered'):
        jsonify(data)

def test_jsonify_type_error(mocker):
    # Mock json.dumps to raise TypeError on first call and succeed on second call
    original_json_dumps = json.dumps

    def side_effect(*args, **kwargs):
        if 'encoding' in kwargs:
            raise TypeError
        return original_json_dumps(*args, **kwargs)

    mocker.patch('json.dumps', side_effect=side_effect)

    data = {"key": b"value"}

    result = jsonify(data)
    assert result == json.dumps({"key": "value"}, default=_json_encode_fallback)
