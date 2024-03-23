# file thonny/roughparse.py:118-159
# lines [118, 119, 140, 141, 142, 144, 145, 147, 149, 150, 152, 153, 155, 156, 158, 159]
# branches []

import pytest
from thonny.roughparse import StringTranslatePseudoMapping

def test_string_translate_pseudo_mapping_getitem():
    preserve_dict = {ord('a'): '1', ord('b'): '2'}
    mapping = StringTranslatePseudoMapping(preserve_dict, '0')
    assert mapping.__getitem__(ord('a')) == '1'
    assert mapping.__getitem__(ord('b')) == '2'
    assert mapping.__getitem__(ord('c')) == '0'

def test_string_translate_pseudo_mapping_len():
    preserve_dict = {ord('a'): '1', ord('b'): '2'}
    mapping = StringTranslatePseudoMapping(preserve_dict, '0')
    assert mapping.__len__() == 2

def test_string_translate_pseudo_mapping_iter():
    preserve_dict = {ord('a'): '1', ord('b'): '2'}
    mapping = StringTranslatePseudoMapping(preserve_dict, '0')
    assert set(mapping.__iter__()) == {ord('a'), ord('b')}

def test_string_translate_pseudo_mapping_get():
    preserve_dict = {ord('a'): '1', ord('b'): '2'}
    mapping = StringTranslatePseudoMapping(preserve_dict, '0')
    assert mapping.get(ord('a')) == '1'
    assert mapping.get(ord('b')) == '2'
    assert mapping.get(ord('c')) == '0'
    # The default parameter for get() is not used because the mapping has its own default
    assert mapping.get(ord('d'), '3') == '0'
