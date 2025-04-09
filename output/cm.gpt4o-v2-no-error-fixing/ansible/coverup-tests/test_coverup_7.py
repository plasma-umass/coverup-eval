# file: lib/ansible/utils/vars.py:97-182
# asked: {"lines": [97, 103, 104, 107, 112, 113, 117, 122, 123, 124, 132, 135, 136, 137, 140, 146, 147, 148, 150, 151, 156, 157, 159, 160, 161, 162, 163, 164, 170, 171, 173, 177, 180, 182], "branches": [[103, 104], [103, 107], [112, 113], [112, 117], [122, 123], [122, 132], [132, 135], [132, 182], [135, 136], [135, 140], [146, 147], [146, 156], [147, 148], [147, 150], [156, 157], [156, 180], [157, 159], [157, 160], [160, 161], [160, 162], [162, 163], [162, 164], [164, 170], [164, 171], [171, 173], [171, 177]]}
# gained: {"lines": [97, 103, 104, 107, 112, 113, 117, 122, 123, 124, 132, 135, 136, 137, 140, 146, 147, 148, 151, 156, 157, 159, 160, 161, 162, 163, 164, 170, 171, 173, 177, 182], "branches": [[103, 104], [103, 107], [112, 113], [112, 117], [122, 123], [122, 132], [132, 135], [132, 182], [135, 136], [135, 140], [146, 147], [146, 156], [147, 148], [156, 157], [157, 159], [157, 160], [160, 161], [160, 162], [162, 163], [162, 164], [164, 170], [164, 171], [171, 173], [171, 177]]}

import pytest
from ansible.errors import AnsibleError
from ansible.utils.vars import merge_hash

def test_merge_hash_invalid_list_merge():
    with pytest.raises(AnsibleError, match="merge_hash: 'list_merge' argument can only be equal to 'replace', 'keep', 'append', 'prepend', 'append_rp' or 'prepend_rp'"):
        merge_hash({}, {}, list_merge='invalid')

def test_merge_hash_empty_x():
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

def test_merge_hash_recursive_dicts():
    x = {'key': {'subkey1': 'value1'}}
    y = {'key': {'subkey2': 'value2'}}
    result = merge_hash(x, y, recursive=True)
    assert result == {'key': {'subkey1': 'value1', 'subkey2': 'value2'}}

def test_merge_hash_non_recursive_dicts():
    x = {'key': {'subkey1': 'value1'}}
    y = {'key': {'subkey2': 'value2'}}
    result = merge_hash(x, y, recursive=False)
    assert result == {'key': {'subkey2': 'value2'}}

def test_merge_hash_replace_lists():
    x = {'key': ['value1']}
    y = {'key': ['value2']}
    result = merge_hash(x, y, list_merge='replace')
    assert result == {'key': ['value2']}

def test_merge_hash_append_lists():
    x = {'key': ['value1']}
    y = {'key': ['value2']}
    result = merge_hash(x, y, list_merge='append')
    assert result == {'key': ['value1', 'value2']}

def test_merge_hash_prepend_lists():
    x = {'key': ['value1']}
    y = {'key': ['value2']}
    result = merge_hash(x, y, list_merge='prepend')
    assert result == {'key': ['value2', 'value1']}

def test_merge_hash_append_rp_lists():
    x = {'key': ['value1', 'value3']}
    y = {'key': ['value2', 'value3']}
    result = merge_hash(x, y, list_merge='append_rp')
    assert result == {'key': ['value1', 'value2', 'value3']}

def test_merge_hash_prepend_rp_lists():
    x = {'key': ['value1', 'value3']}
    y = {'key': ['value2', 'value3']}
    result = merge_hash(x, y, list_merge='prepend_rp')
    assert result == {'key': ['value2', 'value3', 'value1']}

def test_merge_hash_keep_lists():
    x = {'key': ['value1']}
    y = {'key': ['value2']}
    result = merge_hash(x, y, list_merge='keep')
    assert result == {'key': ['value1']}
