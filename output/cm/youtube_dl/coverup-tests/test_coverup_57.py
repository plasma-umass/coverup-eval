# file youtube_dl/swfinterp.py:47-52
# lines [52]
# branches []

import pytest
from youtube_dl.swfinterp import _AVMClass_Object

class MockAVMClass:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def mock_avm_class():
    return MockAVMClass(name="MockClass")

def test_avmclass_object_repr(mock_avm_class):
    avm_class_object = _AVMClass_Object(mock_avm_class)
    expected_repr = "MockClass#%x" % id(avm_class_object)
    assert repr(avm_class_object) == expected_repr
