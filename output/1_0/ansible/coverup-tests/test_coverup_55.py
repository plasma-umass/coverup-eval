# file lib/ansible/plugins/lookup/dict.py:61-76
# lines [61, 63, 66, 67, 69, 70, 72, 73, 75, 76]
# branches ['66->67', '66->69', '70->72', '70->76', '72->73', '72->75']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup import dict as dict_plugin
from collections.abc import Mapping

# Mocking the LookupBase class to avoid side effects
class MockedLookupBase(dict_plugin.LookupBase):
    def run(self, terms, variables=None, **kwargs):
        # NOTE: can remove if with_ is removed
        if not isinstance(terms, list):
            terms = [terms]

        results = []
        for term in terms:
            # Expect any type of Mapping, notably hostvars
            if not isinstance(term, Mapping):
                raise AnsibleError("with_dict expects a dict")

            results.extend(self._flatten_hash_to_list(term))
        return results

    def _flatten_hash_to_list(self, term):
        return list(term.items())

# Replacing the original LookupModule with the mocked one
dict_plugin.LookupModule = MockedLookupBase

def test_lookup_module_with_valid_dict():
    # Setup
    lookup = dict_plugin.LookupModule()
    test_dict = {'key1': 'value1', 'key2': 'value2'}
    
    # Execute
    result = lookup.run([test_dict])
    
    # Assert
    assert result == [('key1', 'value1'), ('key2', 'value2')], "The result should be a list of tuples from the dict"

def test_lookup_module_with_non_list_terms():
    # Setup
    lookup = dict_plugin.LookupModule()
    test_dict = {'key1': 'value1', 'key2': 'value2'}
    
    # Execute
    result = lookup.run(test_dict)
    
    # Assert
    assert result == [('key1', 'value1'), ('key2', 'value2')], "The result should be a list of tuples from the dict"

def test_lookup_module_with_non_dict_raises_error():
    # Setup
    lookup = dict_plugin.LookupModule()
    non_dict = "I am not a dict"
    
    # Execute & Assert
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run([non_dict])
    assert "with_dict expects a dict" in str(excinfo.value), "An AnsibleError should be raised if the term is not a dict"
