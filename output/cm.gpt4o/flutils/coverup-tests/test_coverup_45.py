# file flutils/decorators.py:8-56
# lines [8, 9]
# branches []

import pytest
from flutils.decorators import cached_property

class TestCachedProperty:
    def test_cached_property(self):
        class MyClass:
            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = MyClass()
        assert obj.y == 6  # Check initial computation
        obj.x = 10
        assert obj.y == 6  # Check cached value

        del obj.y  # Delete the cached property
        assert obj.y == 11  # Check recomputation after deletion

    def test_cached_property_reset(self):
        class MyClass:
            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = MyClass()
        assert obj.y == 6  # Check initial computation
        obj.x = 10
        del obj.y  # Delete the cached property
        assert obj.y == 11  # Check recomputation after deletion

    def test_cached_property_multiple_instances(self):
        class MyClass:
            def __init__(self, x):
                self.x = x

            @cached_property
            def y(self):
                return self.x + 1

        obj1 = MyClass(5)
        obj2 = MyClass(10)
        assert obj1.y == 6  # Check initial computation for obj1
        assert obj2.y == 11  # Check initial computation for obj2

        obj1.x = 20
        assert obj1.y == 6  # Check cached value for obj1
        del obj1.y
        assert obj1.y == 21  # Check recomputation after deletion for obj1

        obj2.x = 30
        assert obj2.y == 11  # Check cached value for obj2
        del obj2.y
        assert obj2.y == 31  # Check recomputation after deletion for obj2
