# file: flutils/decorators.py:57-59
# asked: {"lines": [57, 58, 59], "branches": []}
# gained: {"lines": [57, 58, 59], "branches": []}

import pytest
from flutils.decorators import cached_property

class TestCachedProperty:
    def test_init(self):
        def sample_func():
            """Sample docstring"""
            pass

        prop = cached_property(sample_func)
        assert prop.func == sample_func
        assert prop.__doc__ == "Sample docstring"
