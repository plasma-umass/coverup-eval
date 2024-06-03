# file lib/ansible/vars/manager.py:709-755
# lines [709, 710, 717, 719, 720, 722, 723, 725, 726, 727, 729, 730, 732, 733, 735, 736, 738, 739, 741, 742, 744, 745, 747, 748, 751, 752, 754, 755]
# branches []

import pytest
from unittest.mock import patch
from ansible.vars.manager import VarsWithSources

@pytest.fixture
def vars_with_sources():
    data = {'key1': 'value1', 'key2': 'value2'}
    sources = {'key1': 'source1', 'key2': 'source2'}
    return VarsWithSources.new_vars_with_sources(data, sources)

def test_vars_with_sources_getitem(vars_with_sources):
    with patch('ansible.vars.manager.display.debug') as mock_debug:
        assert vars_with_sources['key1'] == 'value1'
        mock_debug.assert_called_with("variable 'key1' from source: source1")

def test_vars_with_sources_setitem(vars_with_sources):
    vars_with_sources['key3'] = 'value3'
    assert vars_with_sources['key3'] == 'value3'

def test_vars_with_sources_delitem(vars_with_sources):
    del vars_with_sources['key1']
    assert 'key1' not in vars_with_sources

def test_vars_with_sources_iter(vars_with_sources):
    keys = list(iter(vars_with_sources))
    assert keys == ['key1', 'key2']

def test_vars_with_sources_len(vars_with_sources):
    assert len(vars_with_sources) == 2

def test_vars_with_sources_contains(vars_with_sources):
    assert 'key1' in vars_with_sources
    assert 'key3' not in vars_with_sources

def test_vars_with_sources_copy(vars_with_sources):
    copy_vars = vars_with_sources.copy()
    assert copy_vars['key1'] == 'value1'
    assert copy_vars.get_source('key1') == 'source1'
    assert copy_vars is not vars_with_sources
    assert copy_vars.data == vars_with_sources.data
    assert copy_vars.sources == vars_with_sources.sources
