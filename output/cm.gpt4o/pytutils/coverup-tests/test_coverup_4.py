# file pytutils/props.py:25-37
# lines [25, 30, 31, 32, 33, 34, 35, 37]
# branches ['33->34', '33->35']

import pytest
from pytutils.props import lazyperclassproperty

class TestLazyPerClassProperty:
    def test_lazyperclassproperty(self):
        class Base:
            @lazyperclassproperty
            def value(cls):
                return cls.__name__

        class Derived(Base):
            pass

        # Ensure the property is computed and cached correctly
        assert Base.value == 'Base'
        assert Derived.value == 'Derived'

        # Ensure the property is cached and not recomputed
        assert Base.value == 'Base'
        assert Derived.value == 'Derived'

        # Ensure the property is separate for each class
        assert Base.value != Derived.value
