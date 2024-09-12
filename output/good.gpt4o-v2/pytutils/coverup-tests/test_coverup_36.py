# file: pytutils/lazy/lazy_regex.py:153-162
# asked: {"lines": [158, 159, 162], "branches": [[158, 159], [158, 162]]}
# gained: {"lines": [158, 159, 162], "branches": [[158, 159], [158, 162]]}

import pytest
import re
from pytutils.lazy.lazy_regex import LazyRegex

class TestLazyRegex:
    @pytest.fixture
    def lazy_regex(self):
        class MockLazyRegex(LazyRegex):
            def __init__(self):
                self._real_regex = None
                self._regex_args = (r'\d+',)
                self._regex_kwargs = {}
                self._regex_attributes_to_copy = ['pattern', 'flags']

            def _real_re_compile(self, *args, **kwargs):
                return re.compile(*args, **kwargs)

        return MockLazyRegex()

    def test_getattr_triggers_compile(self, lazy_regex):
        # Access an attribute to trigger __getattr__
        pattern = lazy_regex.pattern
        assert pattern == r'\d+'
        assert lazy_regex._real_regex is not None

    def test_getattr_returns_attribute(self, lazy_regex):
        # Ensure the regex is compiled
        lazy_regex._compile_and_collapse()
        # Access an attribute to trigger __getattr__
        pattern = lazy_regex.pattern
        assert pattern == r'\d+'

    def test_getattr_missing_attribute(self, lazy_regex):
        # Ensure the regex is compiled
        lazy_regex._compile_and_collapse()
        with pytest.raises(AttributeError):
            lazy_regex.non_existent_attribute
