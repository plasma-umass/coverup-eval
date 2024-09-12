# file: pysnooper/utils.py:10-20
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

from pysnooper.utils import _check_methods

class TestCheckMethods:
    def test_all_methods_present(self):
        class A:
            def method1(self): pass
            def method2(self): pass

        assert _check_methods(A, 'method1', 'method2') == True

    def test_method_not_present(self):
        class A:
            def method1(self): pass

        assert _check_methods(A, 'method1', 'method2') == NotImplemented

    def test_method_is_none(self):
        class A:
            method1 = None
            def method2(self): pass

        assert _check_methods(A, 'method1', 'method2') == NotImplemented

    def test_inherited_method(self):
        class A:
            def method1(self): pass

        class B(A):
            def method2(self): pass

        assert _check_methods(B, 'method1', 'method2') == True

    def test_inherited_method_is_none(self):
        class A:
            method1 = None

        class B(A):
            def method2(self): pass

        assert _check_methods(B, 'method1', 'method2') == NotImplemented
