# file: pytutils/meth.py:1-20
# asked: {"lines": [1, 20], "branches": []}
# gained: {"lines": [1, 20], "branches": []}

import pytest
from pytutils.meth import bind

class TestBind:
    def test_bind_method(self):
        class Foo:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        foo = Foo(2, 3)
        my_unbound_method = lambda self: self.x * self.y
        bind(foo, my_unbound_method, 'multiply')
        
        assert foo.multiply() == 6

    def test_bind_different_method_name(self):
        class Bar:
            def __init__(self, a, b):
                self.a = a
                self.b = b

        bar = Bar(4, 5)
        my_unbound_method = lambda self: self.a + self.b
        bind(bar, my_unbound_method, 'add')
        
        assert bar.add() == 9

    def test_bind_overwrite_existing_method(self):
        class Baz:
            def __init__(self, value):
                self.value = value

            def existing_method(self):
                return self.value

        baz = Baz(10)
        my_unbound_method = lambda self: self.value * 2
        bind(baz, my_unbound_method, 'existing_method')
        
        assert baz.existing_method() == 20
