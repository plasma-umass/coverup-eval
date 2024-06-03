# file lib/ansible/utils/vars.py:97-182
# lines [104, 113, 123, 124, 147, 148, 150, 151, 157, 159, 160, 161, 162, 163, 164, 170, 171, 173, 177]
# branches ['103->104', '112->113', '122->123', '146->147', '147->148', '147->150', '156->157', '157->159', '157->160', '160->161', '160->162', '162->163', '162->164', '164->170', '164->171', '171->173', '171->177']

import pytest
from ansible.errors import AnsibleError
from ansible.utils.vars import merge_hash
from collections.abc import MutableMapping, MutableSequence

def test_merge_hash_invalid_list_merge():
    with pytest.raises(AnsibleError, match="merge_hash: 'list_merge' argument can only be equal to 'replace', 'keep', 'append', 'prepend', 'append_rp' or 'prepend_rp'"):
        merge_hash({}, {}, list_merge='invalid')

def test_merge_hash_x_empty():
    x = {}
    y = {'key': 'value'}
    result = merge_hash(x, y)
    assert result == y

def test_merge_hash_x_equals_y():
    x = {'key': 'value'}
    y = {'key': 'value'}
    result = merge_hash(x, y)
    assert result == y

def test_merge_hash_non_recursive_replace():
    x = {'key1': 'value1'}
    y = {'key2': 'value2'}
    result = merge_hash(x, y, recursive=False, list_merge='replace')
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_merge_hash_recursive_dict():
    x = {'key': {'subkey1': 'value1'}}
    y = {'key': {'subkey2': 'value2'}}
    result = merge_hash(x, y, recursive=True)
    assert result == {'key': {'subkey1': 'value1', 'subkey2': 'value2'}}

def test_merge_hash_non_recursive_dict():
    x = {'key': {'subkey1': 'value1'}}
    y = {'key': {'subkey2': 'value2'}}
    result = merge_hash(x, y, recursive=False)
    assert result == {'key': {'subkey2': 'value2'}}

def test_merge_hash_list_replace():
    x = {'key': [1, 2]}
    y = {'key': [3, 4]}
    result = merge_hash(x, y, list_merge='replace')
    assert result == {'key': [3, 4]}

def test_merge_hash_list_append():
    x = {'key': [1, 2]}
    y = {'key': [3, 4]}
    result = merge_hash(x, y, list_merge='append')
    assert result == {'key': [1, 2, 3, 4]}

def test_merge_hash_list_prepend():
    x = {'key': [1, 2]}
    y = {'key': [3, 4]}
    result = merge_hash(x, y, list_merge='prepend')
    assert result == {'key': [3, 4, 1, 2]}

def test_merge_hash_list_append_rp():
    x = {'key': [1, 2, 3]}
    y = {'key': [3, 4]}
    result = merge_hash(x, y, list_merge='append_rp')
    assert result == {'key': [1, 2, 3, 4]}

def test_merge_hash_list_prepend_rp():
    x = {'key': [1, 2, 3]}
    y = {'key': [3, 4]}
    result = merge_hash(x, y, list_merge='prepend_rp')
    assert result == {'key': [3, 4, 1, 2]}
