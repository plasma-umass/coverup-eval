# file: thonny/roughparse.py:118-159
# asked: {"lines": [118, 119, 140, 141, 142, 144, 145, 147, 149, 150, 152, 153, 155, 156, 158, 159], "branches": []}
# gained: {"lines": [118, 119, 140, 141, 142, 144, 145, 147, 149, 150, 152, 153, 155, 156, 158, 159], "branches": []}

import pytest
from thonny.roughparse import StringTranslatePseudoMapping

@pytest.fixture
def sample_mapping():
    non_defaults = {ord('a'): ord('b'), ord('c'): ord('d')}
    default_value = ord('x')
    return StringTranslatePseudoMapping(non_defaults, default_value)

def test_string_translate_pseudo_mapping_getitem(sample_mapping):
    assert sample_mapping[ord('a')] == ord('b')
    assert sample_mapping[ord('c')] == ord('d')
    assert sample_mapping[ord('e')] == ord('x')

def test_string_translate_pseudo_mapping_len(sample_mapping):
    assert len(sample_mapping) == 2

def test_string_translate_pseudo_mapping_iter(sample_mapping):
    keys = list(iter(sample_mapping))
    assert keys == [ord('a'), ord('c')]

def test_string_translate_pseudo_mapping_get(sample_mapping):
    assert sample_mapping.get(ord('a')) == ord('b')
    assert sample_mapping.get(ord('c')) == ord('d')
    assert sample_mapping.get(ord('e')) == ord('x')
    assert sample_mapping.get(ord('e'), ord('y')) == ord('x')
