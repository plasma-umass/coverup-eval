# file: lib/ansible/plugins/lookup/sequence.py:208-227
# asked: {"lines": [208, 209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227], "branches": [[209, 210], [209, 211], [211, 212], [211, 213], [213, 215], [213, 222], [215, 216], [215, 218], [222, 223], [222, 224], [224, 225], [224, 226], [226, 0], [226, 227]]}
# gained: {"lines": [208, 209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227], "branches": [[209, 210], [209, 211], [211, 212], [211, 213], [213, 215], [213, 222], [215, 216], [215, 218], [222, 223], [222, 224], [224, 225], [224, 226], [226, 0], [226, 227]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

class MockLookupModule(LookupModule):
    def __init__(self, start=None, end=None, count=None, stride=1, format="%d"):
        self.start = start
        self.end = end
        self.count = count
        self.stride = stride
        self.format = format

@pytest.fixture
def lookup_module():
    return MockLookupModule()

def test_sanity_check_no_count_no_end(lookup_module):
    lookup_module.count = None
    lookup_module.end = None
    with pytest.raises(AnsibleError, match="must specify count or end in with_sequence"):
        lookup_module.sanity_check()

def test_sanity_check_both_count_and_end(lookup_module):
    lookup_module.count = 5
    lookup_module.end = 10
    with pytest.raises(AnsibleError, match="can't specify both count and end in with_sequence"):
        lookup_module.sanity_check()

def test_sanity_check_convert_count_to_end(lookup_module):
    lookup_module.start = 1
    lookup_module.count = 5
    lookup_module.end = None
    lookup_module.sanity_check()
    assert lookup_module.end == 5
    assert not hasattr(lookup_module, 'count')

def test_sanity_check_count_zero(lookup_module):
    lookup_module.start = 1
    lookup_module.count = 0
    lookup_module.end = None
    lookup_module.sanity_check()
    assert lookup_module.start == 0
    assert lookup_module.end == 0
    assert lookup_module.stride == 0
    assert not hasattr(lookup_module, 'count')

def test_sanity_check_stride_positive_end_less_than_start(lookup_module):
    lookup_module.start = 10
    lookup_module.end = 5
    lookup_module.stride = 1
    with pytest.raises(AnsibleError, match="to count backwards make stride negative"):
        lookup_module.sanity_check()

def test_sanity_check_stride_negative_end_greater_than_start(lookup_module):
    lookup_module.start = 5
    lookup_module.end = 10
    lookup_module.stride = -1
    with pytest.raises(AnsibleError, match="to count forward don't make stride negative"):
        lookup_module.sanity_check()

def test_sanity_check_bad_format_string(lookup_module):
    lookup_module.start = 1
    lookup_module.end = 1
    lookup_module.format = "%d%d"
    with pytest.raises(AnsibleError, match="bad formatting string: %d%d"):
        lookup_module.sanity_check()
