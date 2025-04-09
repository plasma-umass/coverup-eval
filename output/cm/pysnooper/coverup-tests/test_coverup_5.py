# file pysnooper/utils.py:10-20
# lines [10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
# branches ['12->13', '12->20', '13->14', '13->19', '14->13', '14->15', '15->16', '15->17']

import pytest
from pysnooper.utils import _check_methods

class Base:
    def foo(self):
        pass

class Derived(Base):
    foo = None

class Unrelated:
    bar = None

@pytest.fixture
def cleanup_classes():
    yield
    # Cleanup is not necessary as classes are redefined on each test run

def test_check_methods_with_not_implemented(cleanup_classes):
    assert _check_methods(Derived, 'foo') is NotImplemented
    assert _check_methods(Unrelated, 'bar') is NotImplemented

def test_check_methods_with_true(cleanup_classes):
    assert _check_methods(Base, 'foo') is True
