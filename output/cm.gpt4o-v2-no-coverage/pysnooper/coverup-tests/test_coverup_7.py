# file: pysnooper/utils.py:23-32
# asked: {"lines": [23, 24, 25, 26, 28, 29, 30, 31, 32], "branches": [[30, 31], [30, 32]]}
# gained: {"lines": [23, 24, 25, 28, 29, 30, 31], "branches": [[30, 31]]}

import pytest
import abc
from pysnooper.pycompat import ABC
from pysnooper.utils import WritableStream, _check_methods

class TestWritableStream:
    
    def test_write_abstract_method(self):
        with pytest.raises(TypeError):
            instance = WritableStream()
    
    def test_subclasshook_direct_subclass(self):
        class DirectSubclass(WritableStream):
            def write(self, s):
                pass
        
        assert issubclass(DirectSubclass, WritableStream)
    
    def test_subclasshook_no_write_method(self):
        class NoWriteMethod:
            pass
        
        assert not issubclass(NoWriteMethod, WritableStream)
    
    def test_subclasshook_write_is_none(self):
        class WriteIsNone:
            write = None
        
        assert not issubclass(WriteIsNone, WritableStream)
    
    def test_subclasshook_indirect_subclass(self):
        class IndirectSubclass:
            def write(self, s):
                pass
        
        class AnotherClass(IndirectSubclass, WritableStream):
            pass
        
        assert issubclass(AnotherClass, WritableStream)
    
    def test_check_methods(self):
        class TestClass:
            def write(self, s):
                pass
        
        assert _check_methods(TestClass, 'write') == True
        
        class TestClassWithNone:
            write = None
        
        assert _check_methods(TestClassWithNone, 'write') == NotImplemented
        
        class TestClassWithoutMethod:
            pass
        
        assert _check_methods(TestClassWithoutMethod, 'write') == NotImplemented
