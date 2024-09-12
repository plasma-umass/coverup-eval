# file: pytutils/python.py:5-42
# asked: {"lines": [5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 24, 26, 29, 31, 32, 34, 35, 36, 38, 41, 42], "branches": [[9, 10], [9, 18], [24, 26], [24, 29]]}
# gained: {"lines": [5, 6, 7, 9, 10, 11, 12, 13, 14, 16], "branches": [[9, 10]]}

import pytest
import sys
import types

from pytutils.python import PyInfo

def test_pyinfo_py3_attributes():
    if not PyInfo.PY3:
        pytest.skip("Test only applicable for Python 3")
    
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types == (type,)
    assert PyInfo.maxsize == sys.maxsize

def test_pyinfo_py2_attributes(monkeypatch):
    if not PyInfo.PY2:
        pytest.skip("Test only applicable for Python 2")
    
    monkeypatch.setattr(sys, 'version_info', (2, 7))
    monkeypatch.setattr(sys, 'platform', 'java')
    
    reload(PyInfo)
    
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == int((1 << 31) - 1)

def test_pyinfo_py2_non_java_32bit(monkeypatch):
    if not PyInfo.PY2:
        pytest.skip("Test only applicable for Python 2")
    
    monkeypatch.setattr(sys, 'version_info', (2, 7))
    monkeypatch.setattr(sys, 'platform', 'nonjava')
    
    class X(object):
        def __len__(self):
            return 1 << 31
    
    monkeypatch.setattr(sys, 'maxsize', int((1 << 31) - 1))
    
    reload(PyInfo)
    
    assert PyInfo.maxsize == int((1 << 31) - 1)

def test_pyinfo_py2_non_java_64bit(monkeypatch):
    if not PyInfo.PY2:
        pytest.skip("Test only applicable for Python 2")
    
    monkeypatch.setattr(sys, 'version_info', (2, 7))
    monkeypatch.setattr(sys, 'platform', 'nonjava')
    
    class X(object):
        def __len__(self):
            return 1 << 31
    
    monkeypatch.setattr(sys, 'maxsize', int((1 << 63) - 1))
    
    reload(PyInfo)
    
    assert PyInfo.maxsize == int((1 << 63) - 1)
