# file: lib/ansible/plugins/lookup/sequence.py:143-149
# asked: {"lines": [143, 145, 146, 147, 148, 149], "branches": []}
# gained: {"lines": [143, 145, 146, 147, 148, 149], "branches": []}

import pytest
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_reset(lookup_module):
    lookup_module.reset()
    assert lookup_module.start == 1
    assert lookup_module.count is None
    assert lookup_module.end is None
    assert lookup_module.stride == 1
    assert lookup_module.format == "%d"
