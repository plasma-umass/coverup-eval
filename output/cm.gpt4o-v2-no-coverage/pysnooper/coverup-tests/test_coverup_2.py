# file: pysnooper/utils.py:10-20
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

class TestClassA:
    def method1(self):
        pass

class TestClassB(TestClassA):
    def method2(self):
        pass

class TestClassC:
    method3 = None

def test_check_methods():
    from pysnooper.utils import _check_methods

    # Test case where all methods are found and not None
    assert _check_methods(TestClassB, 'method1', 'method2') == True

    # Test case where a method is not found
    assert _check_methods(TestClassB, 'method1', 'method3') == NotImplemented

    # Test case where a method is found but is None
    assert _check_methods(TestClassC, 'method3') == NotImplemented
