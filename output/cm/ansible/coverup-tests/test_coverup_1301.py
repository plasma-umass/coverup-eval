# file lib/ansible/vars/manager.py:709-755
# lines [730, 739, 742, 745, 748, 752, 755]
# branches []

import pytest
from ansible.vars.manager import VarsWithSources

@pytest.fixture
def vars_with_sources():
    data = {'a': 1, 'b': 2}
    sources = {'a': 'source_a', 'b': 'source_b'}
    return VarsWithSources.new_vars_with_sources(data, sources)

def test_vars_with_sources_coverage(vars_with_sources, mocker):
    # Mock the display object to prevent actual debug output
    mocker.patch('ansible.vars.manager.display')

    # Test __getitem__ and get_source
    assert vars_with_sources['a'] == 1
    assert vars_with_sources.get_source('a') == 'source_a'
    assert vars_with_sources.get_source('c') is None

    # Test __setitem__
    vars_with_sources['c'] = 3
    assert vars_with_sources['c'] == 3

    # Test __delitem__
    del vars_with_sources['c']
    with pytest.raises(KeyError):
        _ = vars_with_sources['c']

    # Test __iter__
    assert set(iter(vars_with_sources)) == {'a', 'b'}

    # Test __len__
    assert len(vars_with_sources) == 2

    # Test __contains__
    assert ('a' in vars_with_sources) is True
    assert ('c' in vars_with_sources) is False

    # Test copy
    new_copy = vars_with_sources.copy()
    assert new_copy['a'] == 1
    assert new_copy.get_source('a') == 'source_a'
    assert new_copy is not vars_with_sources
