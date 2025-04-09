# file: lib/ansible/plugins/lookup/sequence.py:208-227
# asked: {"lines": [209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227], "branches": [[209, 210], [209, 211], [211, 212], [211, 213], [213, 215], [213, 222], [215, 216], [215, 218], [222, 223], [222, 224], [224, 225], [224, 226], [226, 0], [226, 227]]}
# gained: {"lines": [209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227], "branches": [[209, 210], [209, 211], [211, 212], [211, 213], [213, 215], [213, 222], [215, 216], [215, 218], [222, 223], [222, 224], [224, 225], [224, 226], [226, 0], [226, 227]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

class TestLookupModule:
    @pytest.fixture
    def lookup_module(self):
        class MockLookupModule(LookupModule):
            def __init__(self, count=None, end=None, start=0, stride=1, format='%d'):
                self.count = count
                self.end = end
                self.start = start
                self.stride = stride
                self.format = format

            def sanity_check(self):
                super().sanity_check()

        return MockLookupModule

    def test_sanity_check_no_count_no_end(self, lookup_module):
        lm = lookup_module(count=None, end=None)
        with pytest.raises(AnsibleError, match="must specify count or end in with_sequence"):
            lm.sanity_check()

    def test_sanity_check_both_count_and_end(self, lookup_module):
        lm = lookup_module(count=5, end=10)
        with pytest.raises(AnsibleError, match="can't specify both count and end in with_sequence"):
            lm.sanity_check()

    def test_sanity_check_count_to_end_conversion(self, lookup_module):
        lm = lookup_module(count=5, start=1, stride=2)
        lm.sanity_check()
        assert lm.end == 1 + 5 * 2 - 1
        assert not hasattr(lm, 'count')

    def test_sanity_check_count_zero(self, lookup_module):
        lm = lookup_module(count=0)
        lm.sanity_check()
        assert lm.start == 0
        assert lm.end == 0
        assert lm.stride == 0
        assert not hasattr(lm, 'count')

    def test_sanity_check_stride_positive_end_less_than_start(self, lookup_module):
        lm = lookup_module(count=None, start=10, stride=1, end=5)
        with pytest.raises(AnsibleError, match="to count backwards make stride negative"):
            lm.sanity_check()

    def test_sanity_check_stride_negative_end_greater_than_start(self, lookup_module):
        lm = lookup_module(count=None, start=1, stride=-1, end=10)
        with pytest.raises(AnsibleError, match="to count forward don't make stride negative"):
            lm.sanity_check()

    def test_sanity_check_bad_format_string(self, lookup_module):
        lm = lookup_module(count=5, format='bad_format')
        with pytest.raises(AnsibleError, match="bad formatting string: bad_format"):
            lm.sanity_check()
