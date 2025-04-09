# file: thonny/roughparse.py:118-159
# asked: {"lines": [118, 119, 140, 141, 142, 144, 145, 147, 149, 150, 152, 153, 155, 156, 158, 159], "branches": []}
# gained: {"lines": [118, 119, 140, 141, 142, 144, 145, 147, 149, 150, 152, 153, 155, 156, 158, 159], "branches": []}

import pytest
from thonny.roughparse import StringTranslatePseudoMapping

def test_string_translate_pseudo_mapping_getitem():
    non_defaults = {ord('a'): ord('b')}
    default_value = ord('x')
    mapping = StringTranslatePseudoMapping(non_defaults, default_value)
    
    assert mapping[ord('a')] == ord('b')
    assert mapping[ord('c')] == ord('x')

def test_string_translate_pseudo_mapping_len():
    non_defaults = {ord('a'): ord('b'), ord('c'): ord('d')}
    default_value = ord('x')
    mapping = StringTranslatePseudoMapping(non_defaults, default_value)
    
    assert len(mapping) == 2

def test_string_translate_pseudo_mapping_iter():
    non_defaults = {ord('a'): ord('b'), ord('c'): ord('d')}
    default_value = ord('x')
    mapping = StringTranslatePseudoMapping(non_defaults, default_value)
    
    keys = list(iter(mapping))
    assert keys == [ord('a'), ord('c')]

def test_string_translate_pseudo_mapping_get():
    non_defaults = {ord('a'): ord('b')}
    default_value = ord('x')
    mapping = StringTranslatePseudoMapping(non_defaults, default_value)
    
    assert mapping.get(ord('a')) == ord('b')
    assert mapping.get(ord('c')) == ord('x')
    assert mapping.get(ord('c'), ord('y')) == ord('x')
