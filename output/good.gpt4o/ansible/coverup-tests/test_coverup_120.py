# file lib/ansible/plugins/lookup/sequence.py:151-171
# lines [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170]
# branches ['153->154', '153->165', '156->157', '156->158', '165->166', '165->167', '167->exit', '167->168']

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
        "format": "item-%d"
    }
    lookup_module.parse_kv_args(args)
    assert lookup_module.start == 1
    assert lookup_module.end == 10
    assert lookup_module.count == 5
    assert lookup_module.stride == 2
    assert lookup_module.format == "item-%d"

def test_parse_kv_args_invalid_integer(lookup_module):
    args = {
        "start": "one",
        "end": "10"
    }
    with pytest.raises(AnsibleError, match="can't parse start=one as integer"):
        lookup_module.parse_kv_args(args)

def test_parse_kv_args_unrecognized_argument(lookup_module):
    args = {
        "start": "1",
        "end": "10",
        "unknown": "value"
    }
    with pytest.raises(AnsibleError, match="unrecognized arguments to with_sequence: \['unknown'\]"):
        lookup_module.parse_kv_args(args)

def test_parse_kv_args_no_arguments(lookup_module):
    args = {}
    lookup_module.parse_kv_args(args)
    assert not hasattr(lookup_module, 'start')
    assert not hasattr(lookup_module, 'end')
    assert not hasattr(lookup_module, 'count')
    assert not hasattr(lookup_module, 'stride')
    assert not hasattr(lookup_module, 'format')
