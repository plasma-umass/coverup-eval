# file: lib/ansible/vars/manager.py:709-755
# asked: {"lines": [709, 710, 717, 719, 720, 722, 723, 725, 726, 727, 729, 730, 732, 733, 735, 736, 738, 739, 741, 742, 744, 745, 747, 748, 751, 752, 754, 755], "branches": []}
# gained: {"lines": [709, 710, 717, 719, 720, 722, 723, 725, 726, 727, 729, 730, 732, 733, 735, 736, 738, 739, 741, 742, 744, 745, 747, 748, 751, 752, 754, 755], "branches": []}

import pytest
from unittest.mock import patch
from ansible.vars.manager import VarsWithSources

@pytest.fixture
def sample_data():
    return {'key1': 'value1', 'key2': 'value2'}

@pytest.fixture
def sample_sources():
    return {'key1': 'source1', 'key2': 'source2'}

def test_vars_with_sources_init(sample_data):
    vws = VarsWithSources(sample_data)
    assert vws.data == sample_data
    assert vws.sources == {}

def test_vars_with_sources_new_vars_with_sources(sample_data, sample_sources):
    vws = VarsWithSources.new_vars_with_sources(sample_data, sample_sources)
    assert vws.data == sample_data
    assert vws.sources == sample_sources

def test_vars_with_sources_get_source(sample_sources):
    vws = VarsWithSources.new_vars_with_sources({}, sample_sources)
    assert vws.get_source('key1') == 'source1'
    assert vws.get_source('key3') is None

@patch('ansible.vars.manager.display.debug')
def test_vars_with_sources_getitem(mock_debug, sample_data, sample_sources):
    vws = VarsWithSources.new_vars_with_sources(sample_data, sample_sources)
    assert vws['key1'] == 'value1'
    mock_debug.assert_called_with("variable 'key1' from source: source1")

def test_vars_with_sources_setitem(sample_data):
    vws = VarsWithSources(sample_data)
    vws['key3'] = 'value3'
    assert vws['key3'] == 'value3'

def test_vars_with_sources_delitem(sample_data):
    vws = VarsWithSources(sample_data)
    del vws['key1']
    assert 'key1' not in vws

def test_vars_with_sources_iter(sample_data):
    vws = VarsWithSources(sample_data)
    keys = list(iter(vws))
    assert keys == list(sample_data.keys())

def test_vars_with_sources_len(sample_data):
    vws = VarsWithSources(sample_data)
    assert len(vws) == len(sample_data)

def test_vars_with_sources_contains(sample_data):
    vws = VarsWithSources(sample_data)
    assert 'key1' in vws
    assert 'key3' not in vws

def test_vars_with_sources_copy(sample_data, sample_sources):
    vws = VarsWithSources.new_vars_with_sources(sample_data, sample_sources)
    vws_copy = vws.copy()
    assert vws_copy.data == sample_data
    assert vws_copy.sources == sample_sources
    assert vws_copy is not vws
