# file lib/ansible/plugins/lookup/sequence.py:208-227
# lines [208, 209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227]
# branches ['209->210', '209->211', '211->212', '211->213', '213->215', '213->222', '215->216', '215->218', '222->223', '222->224', '224->225', '224->226', '226->exit', '226->227']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

def test_sanity_check_count_and_end_specified(mocker):
    mocker.patch.object(LookupModule, '__init__', return_value=None)
    lookup = LookupModule()
    lookup.count = 1
    lookup.end = 10
    lookup.start = 0
    lookup.stride = 1
    lookup.format = '%d'
    with pytest.raises(AnsibleError, match="can't specify both count and end in with_sequence"):
        lookup.sanity_check()

def test_sanity_check_stride_positive_end_less_than_start(mocker):
    mocker.patch.object(LookupModule, '__init__', return_value=None)
    lookup = LookupModule()
    lookup.count = None
    lookup.end = 0
    lookup.start = 10
    lookup.stride = 1
    lookup.format = '%d'
    with pytest.raises(AnsibleError, match="to count backwards make stride negative"):
        lookup.sanity_check()

def test_sanity_check_stride_negative_end_greater_than_start(mocker):
    mocker.patch.object(LookupModule, '__init__', return_value=None)
    lookup = LookupModule()
    lookup.count = None
    lookup.end = 10
    lookup.start = 0
    lookup.stride = -1
    lookup.format = '%d'
    with pytest.raises(AnsibleError, match="to count forward don't make stride negative"):
        lookup.sanity_check()

def test_sanity_check_bad_format_string(mocker):
    mocker.patch.object(LookupModule, '__init__', return_value=None)
    lookup = LookupModule()
    lookup.count = None
    lookup.end = 10
    lookup.start = 0
    lookup.stride = 1
    lookup.format = 'badformat'
    with pytest.raises(AnsibleError, match="bad formatting string: badformat"):
        lookup.sanity_check()

def test_sanity_check_count_zero(mocker):
    mocker.patch.object(LookupModule, '__init__', return_value=None)
    lookup = LookupModule()
    lookup.count = 0
    lookup.start = 10
    lookup.stride = 1
    lookup.format = '%d'
    lookup.end = None  # Set end to None to avoid AttributeError
    lookup.sanity_check()
    assert lookup.start == 0
    assert lookup.end == 0
    assert lookup.stride == 0
    assert 'count' not in lookup.__dict__
