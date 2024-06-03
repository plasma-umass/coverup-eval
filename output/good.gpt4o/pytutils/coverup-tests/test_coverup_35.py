# file pytutils/lazy/lazy_regex.py:153-162
# lines [158, 159, 162]
# branches ['158->159', '158->162']

import pytest
from unittest.mock import MagicMock

# Assuming LazyRegex is imported from pytutils.lazy.lazy_regex
from pytutils.lazy.lazy_regex import LazyRegex

@pytest.fixture
def lazy_regex():
    class MockLazyRegex(LazyRegex):
        def __init__(self):
            self._real_regex = None

        def _compile_and_collapse(self):
            self._real_regex = MagicMock()
            self._real_regex.some_attr = 'compiled_value'

    return MockLazyRegex()

def test_lazy_regex_getattr_triggers_compile(lazy_regex):
    # Accessing an attribute to trigger __getattr__
    assert lazy_regex.some_attr == 'compiled_value'
    # Ensure _compile_and_collapse was called
    assert lazy_regex._real_regex.some_attr == 'compiled_value'
