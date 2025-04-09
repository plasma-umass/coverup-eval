# file lib/ansible/parsing/utils/jsonify.py:25-38
# lines [28, 29, 31, 32, 33, 35, 36, 37, 38]
# branches ['28->29', '28->31', '32->33', '32->35']

import pytest
import json
from ansible.parsing.utils.jsonify import jsonify

def test_jsonify_none():
    result = jsonify(None)
    assert result == "{}"

def test_jsonify_format_true():
    result = jsonify({"key": "value"}, format=True)
    assert json.loads(result) == {"key": "value"}
    assert result == json.dumps({"key": "value"}, sort_keys=True, indent=4, ensure_ascii=False)

def test_jsonify_format_false():
    result = jsonify({"key": "value"}, format=False)
    assert json.loads(result) == {"key": "value"}
    assert result == json.dumps({"key": "value"}, sort_keys=True, indent=None, ensure_ascii=False)

def test_jsonify_unicode_decode_error(mocker):
    original_json_dumps = json.dumps
    def side_effect(*args, **kwargs):
        if kwargs.get('ensure_ascii') is False:
            raise UnicodeDecodeError("codec", b"", 0, 1, "reason")
        return original_json_dumps(*args, **kwargs)
    
    mocker.patch('json.dumps', side_effect=side_effect)
    result = jsonify({"key": "value"}, format=False)
    assert result == json.dumps({"key": "value"}, sort_keys=True, indent=None)
