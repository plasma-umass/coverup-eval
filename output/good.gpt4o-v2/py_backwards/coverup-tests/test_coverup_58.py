# file: py_backwards/utils/snippet.py:146-157
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

import pytest
from py_backwards.utils.snippet import extend

def test_extend():
    class MockAST:
        def __init__(self):
            self.body = [
                MockAssign('x', 1),
                MockAssign('y', 2)
            ]

    class MockAssign:
        def __init__(self, target, value):
            self.targets = [MockName(target)]
            self.value = MockValue(value)

    class MockName:
        def __init__(self, id):
            self.id = id

    class MockValue:
        def __init__(self, n):
            self.n = n

    vars = MockAST()
    extend(vars)
    # Assertions to verify the postconditions
    assert vars.body[0].targets[0].id == 'x'
    assert vars.body[0].value.n == 1
    assert vars.body[1].targets[0].id == 'y'
    assert vars.body[1].value.n == 2
