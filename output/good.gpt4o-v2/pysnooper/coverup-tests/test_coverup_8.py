# file: pysnooper/utils.py:10-20
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest
from pysnooper.utils import _check_methods

class TestClassA:
    def method1(self):
        pass

class TestClassB:
    method1 = None

class TestClassC:
    pass

def test_check_methods_with_method_present():
    assert _check_methods(TestClassA, 'method1') == True

def test_check_methods_with_method_none():
    assert _check_methods(TestClassB, 'method1') == NotImplemented

def test_check_methods_with_method_absent():
    assert _check_methods(TestClassC, 'method1') == NotImplemented
