# file: youtube_dl/swfinterp.py:66-89
# asked: {"lines": [66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83, 85, 86, 87, 88, 89], "branches": []}
# gained: {"lines": [66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83, 85, 86, 87, 88, 89], "branches": []}

import pytest
from youtube_dl.swfinterp import _AVMClass, _ScopeDict, _AVMClass_Object

def test_avmclass_initialization():
    avm_class = _AVMClass(1, 'TestClass')
    assert avm_class.name_idx == 1
    assert avm_class.name == 'TestClass'
    assert avm_class.method_names == {}
    assert avm_class.method_idxs == {}
    assert avm_class.methods == {}
    assert avm_class.method_pyfunctions == {}
    assert avm_class.static_properties == {}
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.constants == {}

def test_avmclass_make_object():
    avm_class = _AVMClass(1, 'TestClass')
    avm_object = avm_class.make_object()
    assert isinstance(avm_object, _AVMClass_Object)
    assert avm_object.avm_class == avm_class

def test_avmclass_repr():
    avm_class = _AVMClass(1, 'TestClass')
    assert repr(avm_class) == '_AVMClass(TestClass)'

def test_avmclass_register_methods():
    avm_class = _AVMClass(1, 'TestClass')
    methods = {'method1': 1, 'method2': 2}
    avm_class.register_methods(methods)
    assert avm_class.method_names == methods
    assert avm_class.method_idxs == {1: 'method1', 2: 'method2'}
