# file lib/ansible/plugins/filter/mathstuff.py:249-286
# lines [249, 250, 252, 253, 255, 256, 259, 260, 261, 264, 265, 266, 267, 268, 271, 272, 273, 276, 277, 278, 281, 282, 286]
# branches []

import pytest
from ansible.plugins.filter.mathstuff import FilterModule

@pytest.fixture
def filter_module():
    return FilterModule()

def test_filter_module_methods(filter_module):
    filters = filter_module.filters()
    assert 'min' in filters
    assert 'max' in filters
    assert 'log' in filters
    assert 'pow' in filters
    assert 'root' in filters
    assert 'unique' in filters
    assert 'intersect' in filters
    assert 'difference' in filters
    assert 'symmetric_difference' in filters
    assert 'union' in filters
    assert 'product' in filters
    assert 'permutations' in filters
    assert 'combinations' in filters
    assert 'human_readable' in filters
    assert 'human_to_bytes' in filters
    assert 'rekey_on_member' in filters
    assert 'zip' in filters
    assert 'zip_longest' in filters
