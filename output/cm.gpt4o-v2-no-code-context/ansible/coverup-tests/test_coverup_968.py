# file: lib/ansible/vars/manager.py:709-755
# asked: {"lines": [719, 720, 725, 726, 727, 730, 733, 735, 736, 739, 742, 745, 748, 752, 755], "branches": []}
# gained: {"lines": [719, 720, 725, 726, 727, 730, 733, 735, 736, 739, 742, 745, 748, 752, 755], "branches": []}

import pytest
from ansible.vars.manager import VarsWithSources
from unittest.mock import patch

@pytest.fixture
def vars_with_sources():
    return VarsWithSources(a=1, b=2)

def test_vars_with_sources_init():
    vws = VarsWithSources(a=1, b=2)
    assert vws.data == {'a': 1, 'b': 2}
    assert vws.sources == {}

def test_new_vars_with_sources():
    data = {'a': 1, 'b': 2}
    sources = {'a': 'source1', 'b': 'source2'}
    vws = VarsWithSources.new_vars_with_sources(data, sources)
    assert vws.data == data
    assert vws.sources == sources

def test_get_source(vars_with_sources):
    vars_with_sources.sources = {'a': 'source1'}
    assert vars_with_sources.get_source('a') == 'source1'
    assert vars_with_sources.get_source('b') is None

@patch('ansible.vars.manager.display')
def test_getitem(mock_display, vars_with_sources):
    vars_with_sources.sources = {'a': 'source1'}
    assert vars_with_sources['a'] == 1
    mock_display.debug.assert_called_with("variable '%s' from source: %s" % ('a', 'source1'))

def test_setitem(vars_with_sources):
    vars_with_sources['c'] = 3
    assert vars_with_sources.data['c'] == 3

def test_delitem(vars_with_sources):
    del vars_with_sources['a']
    assert 'a' not in vars_with_sources.data

def test_iter(vars_with_sources):
    keys = list(iter(vars_with_sources))
    assert keys == ['a', 'b']

def test_len(vars_with_sources):
    assert len(vars_with_sources) == 2

def test_contains(vars_with_sources):
    assert 'a' in vars_with_sources
    assert 'c' not in vars_with_sources

def test_copy(vars_with_sources):
    vars_with_sources.sources = {'a': 'source1'}
    vws_copy = vars_with_sources.copy()
    assert vws_copy.data == vars_with_sources.data
    assert vws_copy.sources == vars_with_sources.sources
    assert vws_copy is not vars_with_sources
