# file: pymonet/lazy.py:68-78
# asked: {"lines": [78], "branches": []}
# gained: {"lines": [78], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_ap():
    def constructor_fn(x):
        return x + 1

    def applicative_fn(x):
        return x * 2

    lazy_value = Lazy(lambda x: constructor_fn(x))
    applicative = Lazy(lambda x: applicative_fn(x))

    result = lazy_value.ap(applicative)

    assert isinstance(result, Lazy)
    assert result.get(3) == 7  # (3 * 2) + 1

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
