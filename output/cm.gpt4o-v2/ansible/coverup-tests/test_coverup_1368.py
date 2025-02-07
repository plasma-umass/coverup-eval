# file: lib/ansible/module_utils/common/json.py:26-39
# asked: {"lines": [32, 33, 34, 35, 36, 37, 39], "branches": [[32, 33], [32, 34], [34, 35], [34, 36], [36, 37], [36, 39]]}
# gained: {"lines": [32, 33, 34, 35, 36, 37, 39], "branches": [[32, 33], [32, 34], [34, 35], [34, 36], [36, 37], [36, 39]]}

import pytest
from ansible.module_utils.common.json import _preprocess_unsafe_encode
from ansible.module_utils._text import to_text
from ansible.module_utils.common._collections_compat import Mapping
from ansible.module_utils.common.collections import is_sequence

class AnsibleUnsafe(str):
    __UNSAFE__ = True

def _is_unsafe(value):
    return getattr(value, '__UNSAFE__', False) and (not getattr(value, '__ENCRYPTED__', False))

def test_preprocess_unsafe_encode_with_unsafe_string():
    unsafe_value = AnsibleUnsafe("unsafe_string")
    result = _preprocess_unsafe_encode(unsafe_value)
    assert result == {'__ansible_unsafe': to_text(unsafe_value, errors='surrogate_or_strict', nonstring='strict')}

def test_preprocess_unsafe_encode_with_sequence():
    sequence_value = [AnsibleUnsafe("unsafe_string"), "safe_string"]
    result = _preprocess_unsafe_encode(sequence_value)
    assert result == [
        {'__ansible_unsafe': to_text(sequence_value[0], errors='surrogate_or_strict', nonstring='strict')},
        "safe_string"
    ]

def test_preprocess_unsafe_encode_with_mapping():
    mapping_value = {
        "key1": AnsibleUnsafe("unsafe_string"),
        "key2": "safe_string"
    }
    result = _preprocess_unsafe_encode(mapping_value)
    assert result == {
        "key1": {'__ansible_unsafe': to_text(mapping_value["key1"], errors='surrogate_or_strict', nonstring='strict')},
        "key2": "safe_string"
    }
