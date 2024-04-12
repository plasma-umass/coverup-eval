# file pysnooper/utils.py:10-20
# lines [19]
# branches ['13->19', '14->13']

import pytest
from pysnooper.utils import _check_methods

class Base:
    pass

class Derived(Base):
    pass

@pytest.fixture
def clean_base_class():
    # Fixture to clean up any attributes added to Base during tests
    yield
    if hasattr(Base, 'method1'):
        delattr(Base, 'method1')
    if hasattr(Base, 'method2'):
        delattr(Base, 'method2')

def test_check_methods_not_implemented(clean_base_class):
    setattr(Base, 'method1', None)
    assert _check_methods(Derived, 'method1', 'method2') is NotImplemented
