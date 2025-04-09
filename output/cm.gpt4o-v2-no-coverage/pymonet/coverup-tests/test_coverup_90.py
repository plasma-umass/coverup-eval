# file: pymonet/lazy.py:106-115
# asked: {"lines": [106, 113, 115], "branches": []}
# gained: {"lines": [106, 113, 115], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.box import Box

class MockLazy(Lazy):
    def __init__(self):
        super().__init__(lambda: "test_value")
    
    def get(self, *args):
        return self.constructor_fn()

def test_lazy_to_box():
    lazy_instance = MockLazy()
    box_instance = lazy_instance.to_box()
    
    assert isinstance(box_instance, Box)
    assert box_instance.value == "test_value"
