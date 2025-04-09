# file lib/ansible/plugins/lookup/sequence.py:208-227
# lines [208, 209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227]
# branches ['209->210', '209->211', '211->212', '211->213', '213->215', '213->222', '215->216', '215->218', '222->223', '222->224', '224->225', '224->226', '226->exit', '226->227']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    class MockLookupModule(LookupModule):
        def __init__(self, start, end, count, stride, format):
            self.start = start
            self.end = end
            self.count = count
            self.stride = stride
            self.format = format
    return MockLookupModule

def test_sanity_check_no_count_no_end(lookup_module):
    lm = lookup_module(start=0, end=None, count=None, stride=1, format='%d')
    with pytest.raises(AnsibleError, match="must specify count or end in with_sequence"):
        lm.sanity_check()

def test_sanity_check_both_count_and_end(lookup_module):
    lm = lookup_module(start=0, end=10, count=5, stride=1, format='%d')
    with pytest.raises(AnsibleError, match="can't specify both count and end in with_sequence"):
        lm.sanity_check()

def test_sanity_check_count_to_end_conversion(lookup_module):
    lm = lookup_module(start=0, end=None, count=5, stride=1, format='%d')
    lm.sanity_check()
    assert lm.end == 4
    assert not hasattr(lm, 'count')

def test_sanity_check_count_zero(lookup_module):
    lm = lookup_module(start=0, end=None, count=0, stride=1, format='%d')
    lm.sanity_check()
    assert lm.start == 0
    assert lm.end == 0
    assert lm.stride == 0
    assert not hasattr(lm, 'count')

def test_sanity_check_positive_stride_end_less_than_start(lookup_module):
    lm = lookup_module(start=10, end=5, count=None, stride=1, format='%d')
    with pytest.raises(AnsibleError, match="to count backwards make stride negative"):
        lm.sanity_check()

def test_sanity_check_negative_stride_end_greater_than_start(lookup_module):
    lm = lookup_module(start=5, end=10, count=None, stride=-1, format='%d')
    with pytest.raises(AnsibleError, match="to count forward don't make stride negative"):
        lm.sanity_check()

def test_sanity_check_bad_format_string(lookup_module):
    lm = lookup_module(start=0, end=10, count=None, stride=1, format='%d%d')
    with pytest.raises(AnsibleError, match="bad formatting string: %d%d"):
        lm.sanity_check()
