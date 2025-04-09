# file: lib/ansible/plugins/filter/core.py:535-545
# asked: {"lines": [535, 539, 540, 542, 543, 544, 545], "branches": [[539, 540], [539, 542], [543, 544], [543, 545]]}
# gained: {"lines": [535, 539, 540, 542, 543, 544, 545], "branches": [[539, 540], [539, 542], [543, 544], [543, 545]]}

import pytest
from ansible.errors import AnsibleFilterTypeError
from ansible.module_utils.common._collections_compat import Mapping
from ansible.plugins.filter.core import dict_to_list_of_dict_key_value_elements

class TestDictToListOfDictKeyValueElements:
    
    def test_valid_dict(self):
        mydict = {'a': 1, 'b': 2}
        expected = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]
        result = dict_to_list_of_dict_key_value_elements(mydict)
        assert result == expected

    def test_empty_dict(self):
        mydict = {}
        expected = []
        result = dict_to_list_of_dict_key_value_elements(mydict)
        assert result == expected

    def test_invalid_dict(self):
        with pytest.raises(AnsibleFilterTypeError) as excinfo:
            dict_to_list_of_dict_key_value_elements(['not', 'a', 'dict'])
        assert "dict2items requires a dictionary" in str(excinfo.value)

    def test_custom_key_value_names(self):
        mydict = {'a': 1, 'b': 2}
        expected = [{'custom_key': 'a', 'custom_value': 1}, {'custom_key': 'b', 'custom_value': 2}]
        result = dict_to_list_of_dict_key_value_elements(mydict, key_name='custom_key', value_name='custom_value')
        assert result == expected
