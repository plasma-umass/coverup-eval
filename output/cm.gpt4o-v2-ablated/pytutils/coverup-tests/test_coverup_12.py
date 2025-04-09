# file: pytutils/python.py:5-42
# asked: {"lines": [5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 24, 26, 29, 31, 32, 34, 35, 36, 38, 41, 42], "branches": [[9, 10], [9, 18], [24, 26], [24, 29]]}
# gained: {"lines": [5, 6, 7, 9, 10, 11, 12, 13, 14, 16], "branches": [[9, 10]]}

import sys
import types
import pytest

from pytutils.python import PyInfo

def test_pyinfo_py3():
    if sys.version_info[0] == 3:
        assert PyInfo.PY3 is True
        assert PyInfo.PY2 is False
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
        assert PyInfo.maxsize == sys.maxsize

def test_pyinfo_py2(monkeypatch):
    if sys.version_info[0] == 2:
        assert PyInfo.PY3 is False
        assert PyInfo.PY2 is True
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
        
        if sys.platform.startswith("java"):
            assert PyInfo.maxsize == int((1 << 31) - 1)
        else:
            class X(object):
                def __len__(self):
                    return 1 << 31

            try:
                len(X())
            except OverflowError:
                assert PyInfo.maxsize == int((1 << 31) - 1)
            else:
                assert PyInfo.maxsize == int((1 << 63) - 1)

@pytest.mark.skipif(sys.version_info[0] != 2, reason="Only applicable for Python 2")
def test_pyinfo_py2_non_java(monkeypatch):
    monkeypatch.setattr(sys, 'platform', 'non-java-platform')
    class X(object):
        def __len__(self):
            return 1 << 31

    try:
        len(X())
    except OverflowError:
        assert PyInfo.maxsize == int((1 << 31) - 1)
    else:
        assert PyInfo.maxsize == int((1 << 63) - 1)

@pytest.mark.skipif(sys.version_info[0] != 2, reason="Only applicable for Python 2")
def test_pyinfo_py2_java(monkeypatch):
    monkeypatch.setattr(sys, 'platform', 'java')
    assert PyInfo.maxsize == int((1 << 31) - 1)
