# file: lib/ansible/plugins/lookup/together.py:44-67
# asked: {"lines": [44, 45, 52, 53, 54, 55, 56, 57, 59, 61, 63, 64, 65, 67], "branches": [[54, 55], [54, 57], [64, 65], [64, 67]]}
# gained: {"lines": [44, 45, 52, 53, 54, 55, 56, 57, 59, 61, 63, 64, 65, 67], "branches": [[54, 55], [54, 57], [64, 65], [64, 67]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.together import LookupModule

class MockTemplar:
    def template(self, term, fail_on_undefined=True, convert_bare=False):
        return term

class MockLoader:
    pass

@pytest.fixture
def lookup_module():
    return LookupModule(loader=MockLoader(), templar=MockTemplar())

def test_lookup_variables(lookup_module):
    terms = ['a', 'b', 'c']
    result = lookup_module._lookup_variables(terms)
    assert result == [['a'], ['b'], ['c']]

def test_run_empty_terms(lookup_module):
    with pytest.raises(AnsibleError, match="with_together requires at least one element in each list"):
        lookup_module.run([])

def test_run_single_term(lookup_module):
    terms = [['a'], ['b'], ['c']]
    result = lookup_module.run(terms)
    assert result == [['a', 'b', 'c']]

def test_run_multiple_terms(lookup_module):
    terms = [['a', 'b'], ['1', '2']]
    result = lookup_module.run(terms)
    assert result == [['a', '1'], ['b', '2']]

def test_run_uneven_terms(lookup_module):
    terms = [['a', 'b'], ['1']]
    result = lookup_module.run(terms)
    assert result == [['a', '1'], ['b', None]]
