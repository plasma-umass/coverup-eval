# file: lib/ansible/plugins/lookup/dict.py:61-76
# asked: {"lines": [61, 63, 66, 67, 69, 70, 72, 73, 75, 76], "branches": [[66, 67], [66, 69], [70, 72], [70, 76], [72, 73], [72, 75]]}
# gained: {"lines": [61, 63, 66, 67, 69, 70, 72, 73, 75, 76], "branches": [[66, 67], [66, 69], [70, 72], [70, 76], [72, 73], [72, 75]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.dict import LookupModule
from ansible.module_utils.common._collections_compat import Mapping

class TestLookupModule:
    
    @pytest.fixture
    def lookup_module(self):
        return LookupModule()

    def test_run_with_non_list_terms(self, lookup_module):
        terms = {'key': 'value'}
        result = lookup_module.run(terms)
        assert result == [{'key': 'key', 'value': 'value'}]

    def test_run_with_list_of_dicts(self, lookup_module):
        terms = [{'key1': 'value1'}, {'key2': 'value2'}]
        result = lookup_module.run(terms)
        expected = [
            {'key': 'key1', 'value': 'value1'},
            {'key': 'key2', 'value': 'value2'}
        ]
        assert result == expected

    def test_run_with_non_mapping_term(self, lookup_module):
        terms = ['not_a_dict']
        with pytest.raises(AnsibleError, match="with_dict expects a dict"):
            lookup_module.run(terms)

    def test_run_with_empty_list(self, lookup_module):
        terms = []
        result = lookup_module.run(terms)
        assert result == []

    def test_run_with_single_dict(self, lookup_module):
        terms = {'key': 'value'}
        result = lookup_module.run(terms)
        assert result == [{'key': 'key', 'value': 'value'}]
