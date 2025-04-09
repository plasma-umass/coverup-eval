# file tornado/util.py:76-87
# lines [76, 77, 80, 81, 82, 83, 84, 86, 87]
# branches []

import pytest
from tornado.util import ObjectDict

def test_object_dict_getattr():
    obj_dict = ObjectDict()
    obj_dict['key'] = 'value'
    assert obj_dict.key == 'value'

    with pytest.raises(AttributeError):
        _ = obj_dict.non_existent_key

def test_object_dict_setattr():
    obj_dict = ObjectDict()
    obj_dict.key = 'value'
    assert obj_dict['key'] == 'value'

    obj_dict.key = 'new_value'
    assert obj_dict['key'] == 'new_value'
