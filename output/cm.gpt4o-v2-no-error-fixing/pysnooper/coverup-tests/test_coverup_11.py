# file: pysnooper/utils.py:10-20
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

class TestClass:
    def method1(self):
        pass

    def method2(self):
        pass

class TestClassWithNoneMethod:
    def method1(self):
        pass

    method2 = None

class TestClassWithoutMethods:
    pass

def test_check_methods_all_present():
    from pysnooper.utils import _check_methods
    assert _check_methods(TestClass, 'method1', 'method2') is True

def test_check_methods_with_none_method():
    from pysnooper.utils import _check_methods
    assert _check_methods(TestClassWithNoneMethod, 'method1', 'method2') is NotImplemented

def test_check_methods_method_not_present():
    from pysnooper.utils import _check_methods
    assert _check_methods(TestClassWithoutMethods, 'method1') is NotImplemented
