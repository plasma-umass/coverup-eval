# file: lib/ansible/plugins/lookup/sequence.py:151-171
# asked: {"lines": [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170], "branches": [[153, 154], [153, 165], [156, 157], [156, 158], [165, 166], [165, 167], [167, 0], [167, 168]]}
# gained: {"lines": [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170], "branches": [[153, 154], [153, 165], [156, 157], [156, 158], [165, 166], [165, 167], [167, 0], [167, 168]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_parse_kv_args_valid(lookup_module):
    args = {
        "start": "1",
        "end": "10",
        "count": "5",
        "stride": "2",
        "format": "test_format"
    }
    lookup_module.parse_kv_args(args)
    assert lookup_module.start == 1
    assert lookup_module.end == 10
    assert lookup_module.count == 5
    assert lookup_module.stride == 2
    assert lookup_module.format == "test_format"
    assert args == {}

def test_parse_kv_args_invalid_integer(lookup_module):
    args = {
        "start": "one",
    }
    with pytest.raises(AnsibleError, match="can't parse start=one as integer"):
        lookup_module.parse_kv_args(args)

def test_parse_kv_args_unrecognized_argument(lookup_module):
    args = {
        "start": "1",
        "unknown": "value"
    }
    with pytest.raises(AnsibleError, match="unrecognized arguments to with_sequence: \['unknown'\]"):
        lookup_module.parse_kv_args(args)

def test_parse_kv_args_missing_optional_args(lookup_module):
    args = {
        "start": "1",
        "end": "10"
    }
    lookup_module.parse_kv_args(args)
    assert lookup_module.start == 1
    assert lookup_module.end == 10
    assert args == {}
