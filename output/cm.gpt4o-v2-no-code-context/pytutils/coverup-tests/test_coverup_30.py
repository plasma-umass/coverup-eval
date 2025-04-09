# file: pytutils/lazy/lazy_regex.py:153-162
# asked: {"lines": [153, 158, 159, 162], "branches": [[158, 159], [158, 162]]}
# gained: {"lines": [153, 158, 159, 162], "branches": [[158, 159], [158, 162]]}

import pytest
from pytutils.lazy.lazy_regex import LazyRegex

class MockRegex:
    def __init__(self):
        self.some_attr = "mocked"

class TestLazyRegex(LazyRegex):
    def _compile_and_collapse(self):
        self._real_regex = MockRegex()

@pytest.fixture
def lazy_regex():
    return TestLazyRegex()

def test_lazy_regex_getattr_compile(lazy_regex):
    # Accessing an attribute to trigger __getattr__ and compile
    assert lazy_regex.some_attr == "mocked"

def test_lazy_regex_getattr_no_compile(lazy_regex):
    # Manually setting _real_regex to bypass compilation
    lazy_regex._real_regex = MockRegex()
    assert lazy_regex.some_attr == "mocked"
