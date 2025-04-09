# file: pymonet/lazy.py:27-36
# asked: {"lines": [27, 31, 32, 33, 34, 35], "branches": []}
# gained: {"lines": [27, 31, 32, 33, 34, 35], "branches": []}

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    def test_lazy_eq_same_instance(self):
        def constructor_fn():
            return 42

        lazy1 = Lazy(constructor_fn)
        lazy2 = Lazy(constructor_fn)
        
        # Force evaluation
        lazy1.value
        lazy2.value
        
        assert lazy1 == lazy2

    def test_lazy_eq_different_instance(self):
        def constructor_fn1():
            return 42

        def constructor_fn2():
            return 42

        lazy1 = Lazy(constructor_fn1)
        lazy2 = Lazy(constructor_fn2)
        
        # Force evaluation
        lazy1.value
        lazy2.value
        
        assert lazy1 != lazy2

    def test_lazy_eq_not_evaluated(self):
        def constructor_fn():
            return 42

        lazy1 = Lazy(constructor_fn)
        lazy2 = Lazy(constructor_fn)
        
        assert lazy1 == lazy2

    def test_lazy_eq_different_value(self):
        def constructor_fn1():
            return 42

        def constructor_fn2():
            return 43

        lazy1 = Lazy(constructor_fn1)
        lazy2 = Lazy(constructor_fn2)
        
        # Force evaluation
        lazy1.value
        lazy2.value
        
        assert lazy1 != lazy2

    def test_lazy_eq_different_type(self):
        def constructor_fn():
            return 42

        lazy1 = Lazy(constructor_fn)
        other = 42
        
        assert lazy1 != other
