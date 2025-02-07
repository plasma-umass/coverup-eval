# file: pymonet/lazy.py:24-25
# asked: {"lines": [24, 25], "branches": []}
# gained: {"lines": [24, 25], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_str():
    def sample_fn(x):
        return x * 2

    lazy_instance = Lazy(sample_fn)
    lazy_instance.value = 10
    lazy_instance.is_evaluated = True

    expected_str = 'Lazy[fn={}, value={}, is_evaluated={}]'.format(sample_fn, 10, True)
    assert str(lazy_instance) == expected_str
