# file youtube_dl/swfinterp.py:66-89
# lines [66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83, 85, 86, 87, 88, 89]
# branches []

import pytest
from youtube_dl.swfinterp import _AVMClass

@pytest.fixture
def avm_class():
    return _AVMClass(name_idx=1, name='TestClass')

def test_avm_class_register_methods(avm_class):
    methods = {'method1': 2, 'method2': 3}
    avm_class.register_methods(methods)
    assert avm_class.method_names == methods
    assert avm_class.method_idxs == {2: 'method1', 3: 'method2'}

def test_avm_class_repr(avm_class):
    assert repr(avm_class) == '_AVMClass(TestClass)'

def test_avm_class_make_object(avm_class):
    obj = avm_class.make_object()
    assert obj.__class__.__name__ == '_AVMClass_Object'
    assert obj.avm_class == avm_class
