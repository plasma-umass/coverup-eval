# file lib/ansible/vars/manager.py:54-72
# lines [54, 61, 62, 63, 64, 66, 68, 69, 70, 72]
# branches ['61->62', '61->63', '63->64', '63->66', '68->69', '68->72', '69->68', '69->70']

import pytest
from ansible.vars.manager import preprocess_vars
from ansible.errors import AnsibleError
from collections.abc import MutableMapping

def test_preprocess_vars_none():
    assert preprocess_vars(None) is None

def test_preprocess_vars_not_list():
    result = preprocess_vars({'key': 'value'})
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == {'key': 'value'}

def test_preprocess_vars_list_of_dicts():
    input_data = [{'key1': 'value1'}, {'key2': 'value2'}]
    result = preprocess_vars(input_data)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result == input_data

def test_preprocess_vars_invalid_type():
    with pytest.raises(AnsibleError, match="variable files must contain either a dictionary of variables, or a list of dictionaries. Got:"):
        preprocess_vars('invalid_string')

def test_preprocess_vars_list_with_invalid_type():
    with pytest.raises(AnsibleError, match="variable files must contain either a dictionary of variables, or a list of dictionaries. Got:"):
        preprocess_vars(['valid_dict', 123])

@pytest.fixture(autouse=True)
def cleanup():
    # Any necessary cleanup code can be added here
    yield
    # Cleanup code to ensure no side effects
