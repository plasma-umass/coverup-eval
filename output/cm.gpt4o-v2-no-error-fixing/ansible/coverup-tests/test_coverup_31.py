# file: lib/ansible/plugins/lookup/sequence.py:208-227
# asked: {"lines": [208, 209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227], "branches": [[209, 210], [209, 211], [211, 212], [211, 213], [213, 215], [213, 222], [215, 216], [215, 218], [222, 223], [222, 224], [224, 225], [224, 226], [226, 0], [226, 227]]}
# gained: {"lines": [208, 209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227], "branches": [[209, 210], [209, 211], [211, 212], [211, 213], [213, 215], [213, 222], [215, 216], [215, 218], [222, 223], [222, 224], [224, 225], [224, 226], [226, 0], [226, 227]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    class MockLookupModule(LookupModule):
        def __init__(self, start, count, end, stride, format):
            self.start = start
            self.count = count
            self.end = end
            self.stride = stride
            self.format = format
    return MockLookupModule

def test_sanity_check_no_count_no_end(lookup_module):
    module = lookup_module(start=0, count=None, end=None, stride=1, format='%d')
    with pytest.raises(AnsibleError, match="must specify count or end in with_sequence"):
        module.sanity_check()

def test_sanity_check_both_count_and_end(lookup_module):
    module = lookup_module(start=0, count=5, end=10, stride=1, format='%d')
    with pytest.raises(AnsibleError, match="can't specify both count and end in with_sequence"):
        module.sanity_check()

def test_sanity_check_convert_count_to_end(lookup_module):
    module = lookup_module(start=0, count=5, end=None, stride=1, format='%d')
    module.sanity_check()
    assert module.end == 4
    assert not hasattr(module, 'count')

def test_sanity_check_count_zero(lookup_module):
    module = lookup_module(start=0, count=0, end=None, stride=1, format='%d')
    module.sanity_check()
    assert module.start == 0
    assert module.end == 0
    assert module.stride == 0
    assert not hasattr(module, 'count')

def test_sanity_check_stride_positive_end_less_than_start(lookup_module):
    module = lookup_module(start=10, count=None, end=5, stride=1, format='%d')
    with pytest.raises(AnsibleError, match="to count backwards make stride negative"):
        module.sanity_check()

def test_sanity_check_stride_negative_end_greater_than_start(lookup_module):
    module = lookup_module(start=0, count=None, end=10, stride=-1, format='%d')
    with pytest.raises(AnsibleError, match="to count forward don't make stride negative"):
        module.sanity_check()

def test_sanity_check_bad_formatting_string(lookup_module):
    module = lookup_module(start=0, count=None, end=10, stride=1, format='bad_format')
    with pytest.raises(AnsibleError, match="bad formatting string: bad_format"):
        module.sanity_check()
