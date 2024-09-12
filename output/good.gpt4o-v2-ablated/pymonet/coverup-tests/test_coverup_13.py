# file: pymonet/lazy.py:95-104
# asked: {"lines": [95, 102, 103, 104], "branches": [[102, 103], [102, 104]]}
# gained: {"lines": [95, 102, 103, 104], "branches": [[102, 103], [102, 104]]}

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    @pytest.fixture
    def lazy_instance(self):
        class TestLazy(Lazy):
            def __init__(self):
                self.is_evaluated = False
                self.value = None

            def _compute_value(self, *args):
                self.is_evaluated = True
                self.value = sum(args)
                return self.value

        return TestLazy()

    def test_get_not_evaluated(self, lazy_instance):
        result = lazy_instance.get(1, 2, 3)
        assert result == 6
        assert lazy_instance.is_evaluated
        assert lazy_instance.value == 6

    def test_get_already_evaluated(self, lazy_instance):
        lazy_instance.is_evaluated = True
        lazy_instance.value = 10
        result = lazy_instance.get(1, 2, 3)
        assert result == 10
        assert lazy_instance.is_evaluated
        assert lazy_instance.value == 10
