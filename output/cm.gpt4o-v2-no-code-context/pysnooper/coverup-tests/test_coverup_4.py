# file: pysnooper/utils.py:10-20
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

from pysnooper.utils import _check_methods

class DummyClassWithMethods:
    def method1(self):
        pass

    def method2(self):
        pass

class DummyClassWithNoneMethod:
    def method1(self):
        pass

    method2 = None

class DummyClassWithoutMethods:
    pass

def test_check_methods_all_present():
    assert _check_methods(DummyClassWithMethods, 'method1', 'method2') == True

def test_check_methods_with_none_method():
    assert _check_methods(DummyClassWithNoneMethod, 'method1', 'method2') == NotImplemented

def test_check_methods_not_present():
    assert _check_methods(DummyClassWithoutMethods, 'method1') == NotImplemented
