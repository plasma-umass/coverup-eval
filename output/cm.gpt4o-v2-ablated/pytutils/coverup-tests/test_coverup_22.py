# file: pytutils/props.py:25-37
# asked: {"lines": [30, 31, 32, 33, 34, 35, 37], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [30, 31, 32, 33, 34, 35, 37], "branches": [[33, 34], [33, 35]]}

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

        # Test that the property is correctly set and cached for Base
        assert Base.value == 'Base'
        assert hasattr(Base, '_Base_lazy_value')
        assert Base._Base_lazy_value == 'Base'

        # Test that the property is correctly set and cached for Derived
        assert Derived.value == 'Derived'
        assert hasattr(Derived, '_Derived_lazy_value')
        assert Derived._Derived_lazy_value == 'Derived'

        # Ensure that the cached values are used
        Base._Base_lazy_value = 'ModifiedBase'
        Derived._Derived_lazy_value = 'ModifiedDerived'
        assert Base.value == 'ModifiedBase'
        assert Derived.value == 'ModifiedDerived'
