# file py_backwards/transformers/six_moves.py:7-18
# lines [7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18]
# branches ['10->11', '10->12', '13->14', '13->18', '14->15', '14->17']

import pytest
from py_backwards.transformers.six_moves import MovedAttribute

def test_moved_attribute():
    # Test with name, old_mod, and new_mod provided
    attr1 = MovedAttribute(name='urllib', old_mod='old_urllib', new_mod=None)
    assert attr1.name == 'urllib'
    assert attr1.new_mod == 'urllib'
    assert attr1.new_attr == 'urllib'

    # Test with name, old_mod, new_mod, and old_attr provided
    attr2 = MovedAttribute(name='urllib', old_mod='old_urllib', new_mod=None, old_attr='old_urllib2')
    assert attr2.name == 'urllib'
    assert attr2.new_mod == 'urllib'
    assert attr2.new_attr == 'old_urllib2'

    # Test with all parameters provided
    attr3 = MovedAttribute(name='urllib', old_mod='old_urllib', new_mod='new_urllib', old_attr='old_urllib2', new_attr='new_urllib2')
    assert attr3.name == 'urllib'
    assert attr3.new_mod == 'new_urllib'
    assert attr3.new_attr == 'new_urllib2'
