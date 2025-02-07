# file: lib/ansible/plugins/lookup/sequence.py:151-171
# asked: {"lines": [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170], "branches": [[153, 154], [153, 165], [156, 157], [156, 158], [165, 166], [165, 167], [167, 0], [167, 168]]}
# gained: {"lines": [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170], "branches": [[153, 154], [153, 165], [156, 157], [156, 158], [165, 166], [165, 167], [167, 0], [167, 168]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    module = LookupModule()
    module.start = None
    module.end = None
    module.count = None
    module.stride = None
    module.format = None
    return module

def test_parse_kv_args_valid(lookup_module):
    args = {
        'start': '10',
        'end': '20',
        'count': '5',
        'stride': '2',
        'format': '%02d'
    }
    lookup_module.parse_kv_args(args)
    assert lookup_module.start == 10
    assert lookup_module.end == 20
    assert lookup_module.count == 5
    assert lookup_module.stride == 2
    assert lookup_module.format == '%02d'

def test_parse_kv_args_invalid_integer(lookup_module):
    args = {
        'start': '10',
        'end': 'invalid',
    }
    with pytest.raises(AnsibleError, match="can't parse end=invalid as integer"):
        lookup_module.parse_kv_args(args)

def test_parse_kv_args_unrecognized_argument(lookup_module):
    args = {
        'start': '10',
        'unknown': 'value'
    }
    with pytest.raises(AnsibleError, match="unrecognized arguments to with_sequence: \['unknown'\]"):
        lookup_module.parse_kv_args(args)

def test_parse_kv_args_no_arguments(lookup_module):
    args = {}
    lookup_module.parse_kv_args(args)
    assert lookup_module.start is None
    assert lookup_module.end is None
    assert lookup_module.count is None
    assert lookup_module.stride is None
    assert lookup_module.format is None
