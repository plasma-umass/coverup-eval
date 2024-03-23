# file lib/ansible/utils/vars.py:97-182
# lines [104, 113, 150, 159, 162, 163, 164, 170, 171, 173, 180]
# branches ['103->104', '112->113', '147->150', '156->180', '157->159', '160->162', '162->163', '162->164', '164->170', '164->171', '171->173', '171->177']

import pytest
from ansible.errors import AnsibleError
from ansible.utils.vars import merge_hash
from collections.abc import MutableMapping, MutableSequence

def test_merge_hash_coverage(mocker):
    # Test invalid list_merge argument
    with pytest.raises(AnsibleError):
        merge_hash({}, {}, list_merge='invalid')

    # Test x is empty or x equals y
    assert merge_hash({}, {}) == {}
    assert merge_hash({'a': 1}, {'a': 1}) == {'a': 1}

    # Test non-recursive merge
    assert merge_hash({'a': 1}, {'b': 2}, recursive=False) == {'a': 1, 'b': 2}

    # Test recursive merge with non-dict values
    assert merge_hash({'a': 1}, {'a': 2}, recursive=True) == {'a': 2}

    # Test recursive merge with dict values
    assert merge_hash({'a': {'b': 1}}, {'a': {'c': 2}}, recursive=True) == {'a': {'b': 1, 'c': 2}}

    # Test non-recursive merge with dict values
    assert merge_hash({'a': {'b': 1}}, {'a': {'c': 2}}, recursive=False) == {'a': {'c': 2}}

    # Test list merge with 'replace'
    assert merge_hash({'a': [1]}, {'a': [2]}, list_merge='replace') == {'a': [2]}

    # Test list merge with 'append'
    assert merge_hash({'a': [1]}, {'a': [2]}, list_merge='append') == {'a': [1, 2]}

    # Test list merge with 'prepend'
    assert merge_hash({'a': [1]}, {'a': [2]}, list_merge='prepend') == {'a': [2, 1]}

    # Test list merge with 'append_rp'
    assert merge_hash({'a': [1, 2]}, {'a': [2, 3]}, list_merge='append_rp') == {'a': [1, 2, 3]}

    # Test list merge with 'prepend_rp'
    assert merge_hash({'a': [1, 2]}, {'a': [2, 3]}, list_merge='prepend_rp') == {'a': [2, 3, 1]}

    # Test list merge with 'keep'
    assert merge_hash({'a': [1]}, {'a': [2]}, list_merge='keep') == {'a': [1]}

    # Test merge with non-list, non-dict values
    assert merge_hash({'a': 1}, {'a': 'b'}) == {'a': 'b'}
