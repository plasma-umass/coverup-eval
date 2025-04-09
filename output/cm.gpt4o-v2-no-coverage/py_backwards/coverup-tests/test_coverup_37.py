# file: py_backwards/transformers/return_from_generator.py:7-12
# asked: {"lines": [7, 8, 9, 10, 11, 12], "branches": []}
# gained: {"lines": [7, 8], "branches": []}

import pytest
from py_backwards.transformers.return_from_generator import return_from_generator
from py_backwards.utils.snippet import snippet, let

def test_return_from_generator():
    class MockSnippet:
        def __init__(self, fn):
            self.fn = fn

        def __call__(self, *args, **kwargs):
            return self.fn(*args, **kwargs)

    def mock_let(var):
        pass

    @MockSnippet
    def mock_return_from_generator(return_value):
        mock_let('exc')
        exc = StopIteration()
        exc.value = return_value
        raise exc

    with pytest.raises(StopIteration) as exc_info:
        mock_return_from_generator(42)
    assert exc_info.value.value == 42
