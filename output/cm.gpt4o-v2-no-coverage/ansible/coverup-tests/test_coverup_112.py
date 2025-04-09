# file: lib/ansible/plugins/lookup/varnames.py:54-79
# asked: {"lines": [54, 56, 58, 59, 61, 63, 64, 65, 67, 68, 70, 71, 72, 73, 75, 76, 77, 79], "branches": [[58, 59], [58, 61], [65, 67], [65, 79], [67, 68], [67, 70], [75, 65], [75, 76], [76, 75], [76, 77]]}
# gained: {"lines": [54, 56, 58, 59, 61, 63, 64, 65, 67, 68, 70, 71, 72, 73, 75, 76, 77, 79], "branches": [[58, 59], [58, 61], [65, 67], [65, 79], [67, 68], [67, 70], [75, 65], [75, 76], [76, 75], [76, 77]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.varnames import LookupModule

class MockLookupModule(LookupModule):
    def __init__(self, loader=None, templar=None, **kwargs):
        super(MockLookupModule, self).__init__(loader, templar, **kwargs)
        self._load_name = 'mock_lookup'

def test_run_no_variables():
    lookup = MockLookupModule()
    with pytest.raises(AnsibleError, match='No variables available to search'):
        lookup.run(['term'])

def test_run_invalid_term_type():
    lookup = MockLookupModule()
    with pytest.raises(AnsibleError, match='Invalid setting identifier'):
        lookup.run([123], variables={'var1': 'value1'})

def test_run_invalid_regex():
    lookup = MockLookupModule()
    with pytest.raises(AnsibleError, match='Unable to use'):
        lookup.run(['[invalid'], variables={'var1': 'value1'})

def test_run_no_match():
    lookup = MockLookupModule()
    result = lookup.run(['nomatch'], variables={'var1': 'value1'})
    assert result == []

def test_run_match():
    lookup = MockLookupModule()
    result = lookup.run(['var'], variables={'var1': 'value1', 'var2': 'value2', 'other': 'value3'})
    assert result == ['var1', 'var2']
