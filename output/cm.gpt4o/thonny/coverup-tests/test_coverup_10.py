# file thonny/roughparse.py:118-159
# lines [118, 119, 140, 141, 142, 144, 145, 147, 149, 150, 152, 153, 155, 156, 158, 159]
# branches []

import pytest
from thonny.roughparse import StringTranslatePseudoMapping

def test_string_translate_pseudo_mapping():
    # Test initialization and basic functionality
    whitespace_chars = ' \t\n\r'
    preserve_dict = {ord(c): ord(c) for c in whitespace_chars}
    default_value = ord('x')
    mapping = StringTranslatePseudoMapping(preserve_dict, default_value)
    
    # Test __getitem__
    assert mapping[ord(' ')] == ord(' ')
    assert mapping[ord('a')] == ord('x')
    
    # Test get method
    assert mapping.get(ord(' ')) == ord(' ')
    assert mapping.get(ord('a')) == ord('x')
    assert mapping.get(ord('a'), ord('y')) == ord('x')  # default value should be ignored
    
    # Test __len__
    assert len(mapping) == len(preserve_dict)
    
    # Test __iter__
    assert set(iter(mapping)) == set(preserve_dict.keys())
    
    # Test str.translate with the mapping
    text = "a + b\tc\nd"
    translated_text = text.translate(mapping)
    assert translated_text == 'x x x\tx\nx'

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # No specific cleanup required for this test
