# file: tornado/util.py:76-87
# asked: {"lines": [76, 77, 80, 81, 82, 83, 84, 86, 87], "branches": []}
# gained: {"lines": [76, 77, 80, 81, 82, 83, 84, 86, 87], "branches": []}

import pytest
from tornado.util import ObjectDict

def test_objectdict_getattr_existing_key():
    obj_dict = ObjectDict()
    obj_dict['key'] = 'value'
    assert obj_dict.key == 'value'

def test_objectdict_getattr_non_existing_key():
    obj_dict = ObjectDict()
    with pytest.raises(AttributeError) as excinfo:
        _ = obj_dict.non_existing_key
    assert str(excinfo.value) == 'non_existing_key'

def test_objectdict_setattr():
    obj_dict = ObjectDict()
    obj_dict.new_key = 'new_value'
    assert obj_dict['new_key'] == 'new_value'
    assert obj_dict.new_key == 'new_value'
