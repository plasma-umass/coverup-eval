# file pysnooper/variables.py:86-97
# lines [86, 87, 88, 89, 90, 93, 94, 96, 97]
# branches []

import itertools
import pytest
from pysnooper.variables import Attrs

class DummyWithDict:
    def __init__(self):
        self.a = 1
        self.b = 2

class DummyWithSlots:
    __slots__ = ['x', 'y']
    def __init__(self):
        self.x = 3
        self.y = 4

@pytest.fixture
def dummy_with_dict():
    return DummyWithDict()

@pytest.fixture
def dummy_with_slots():
    return DummyWithSlots()

def test_attrs_with_dict(dummy_with_dict, mocker):
    mocker.patch('pysnooper.variables.CommonVariable.__init__', return_value=None)
    attrs = Attrs('dummy_source')
    keys = list(attrs._keys(dummy_with_dict))
    assert 'a' in keys
    assert 'b' in keys
    assert attrs._format_key('a') == '.a'
    assert attrs._get_value(dummy_with_dict, 'a') == 1

def test_attrs_with_slots(dummy_with_slots, mocker):
    mocker.patch('pysnooper.variables.CommonVariable.__init__', return_value=None)
    attrs = Attrs('dummy_source')
    keys = list(attrs._keys(dummy_with_slots))
    assert 'x' in keys
    assert 'y' in keys
    assert attrs._format_key('x') == '.x'
    assert attrs._get_value(dummy_with_slots, 'x') == 3
