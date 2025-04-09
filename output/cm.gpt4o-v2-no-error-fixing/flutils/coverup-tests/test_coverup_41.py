# file: flutils/objutils.py:116-143
# asked: {"lines": [138, 139, 140, 141, 142, 143], "branches": [[138, 139], [138, 143], [139, 140], [139, 142], [140, 139], [140, 141]]}
# gained: {"lines": [138, 139, 140, 141, 142, 143], "branches": [[138, 139], [138, 143], [139, 140], [139, 142], [140, 139], [140, 141]]}

import pytest
from flutils.objutils import has_callables

class TestHasCallables:
    def test_has_callables_all_callable(self):
        class TestClass:
            def method1(self): pass
            def method2(self): pass

        obj = TestClass()
        assert has_callables(obj, 'method1', 'method2') is True

    def test_has_callables_not_all_callable(self):
        class TestClass:
            def method1(self): pass
            method2 = "not a callable"

        obj = TestClass()
        assert has_callables(obj, 'method1', 'method2') is False

    def test_has_callables_missing_attr(self):
        class TestClass:
            def method1(self): pass

        obj = TestClass()
        assert has_callables(obj, 'method1', 'method2') is False
