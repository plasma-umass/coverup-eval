# file: tornado/util.py:76-87
# asked: {"lines": [81, 82, 83, 84, 87], "branches": []}
# gained: {"lines": [81, 82, 83, 84, 87], "branches": []}

import pytest
from typing import Any
from tornado.util import ObjectDict

def test_objectdict_getattr_existing_key():
    obj = ObjectDict()
    obj['key'] = 'value'
    assert obj.key == 'value'

def test_objectdict_getattr_nonexistent_key():
    obj = ObjectDict()
    with pytest.raises(AttributeError) as excinfo:
        _ = obj.nonexistent_key
    assert str(excinfo.value) == 'nonexistent_key'

def test_objectdict_setattr():
    obj = ObjectDict()
    obj.key = 'value'
    assert obj['key'] == 'value'
    assert obj.key == 'value'
