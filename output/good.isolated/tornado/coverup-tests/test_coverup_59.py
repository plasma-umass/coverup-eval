# file tornado/util.py:76-87
# lines [76, 77, 80, 81, 82, 83, 84, 86, 87]
# branches []

import pytest
from tornado.util import ObjectDict

def test_object_dict_getattr():
    obj_dict = ObjectDict()
    obj_dict['key'] = 'value'
    
    # Test __getattr__ for existing key
    assert obj_dict.key == 'value'
    
    # Test __getattr__ for non-existing key
    with pytest.raises(AttributeError):
        _ = obj_dict.non_existing_key

def test_object_dict_setattr():
    obj_dict = ObjectDict()
    
    # Test __setattr__
    obj_dict.new_key = 'new_value'
    assert obj_dict['new_key'] == 'new_value'
