# file lib/ansible/plugins/lookup/sequence.py:208-227
# lines [210, 216]
# branches ['209->210', '215->216']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

def test_sequence_sanity_check_count_and_end_not_specified():
    lookup = LookupModule()
    lookup.count = None
    lookup.end = None
    lookup.format = "%d"  # Assuming a default format is needed
    with pytest.raises(AnsibleError) as excinfo:
        lookup.sanity_check()
    assert "must specify count or end in with_sequence" in str(excinfo.value)

def test_sequence_sanity_check_count_not_zero():
    lookup = LookupModule()
    lookup.start = 1
    lookup.count = 5
    lookup.stride = 1
    lookup.end = None
    lookup.format = "%d"  # Assuming a default format is needed
    lookup.sanity_check()
    assert lookup.end == 5
