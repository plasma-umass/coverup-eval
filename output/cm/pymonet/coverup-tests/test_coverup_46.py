# file pymonet/lazy.py:80-93
# lines [80, 89, 90, 91, 93]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_bind():
    def constructor_fn():
        return "initial_value"

    def bind_fn(value):
        assert value == "initial_value"
        return Lazy(lambda: value + "_bound")

    lazy_instance = Lazy(constructor_fn)
    bound_lazy = lazy_instance.bind(bind_fn)

    assert callable(bound_lazy.constructor_fn)
    assert bound_lazy.constructor_fn()() == "initial_value_bound"

def test_lazy_bind_with_args():
    def constructor_fn(x, y):
        return x + y

    def bind_fn(value):
        assert value == 3
        return Lazy(lambda: value * 2)

    lazy_instance = Lazy(constructor_fn)
    bound_lazy = lazy_instance.bind(bind_fn)

    assert callable(bound_lazy.constructor_fn)
    assert bound_lazy.constructor_fn(1, 2)() == 6

@pytest.fixture
def mock_lazy(mocker):
    return mocker.patch('pymonet.lazy.Lazy', autospec=True)

def test_lazy_bind_with_mock(mock_lazy):
    def constructor_fn():
        return "initial_value"

    def bind_fn(value):
        return mock_lazy(lambda: value + "_bound")

    lazy_instance = Lazy(constructor_fn)
    lazy_instance.bind(bind_fn)

    mock_lazy.assert_called_once()
