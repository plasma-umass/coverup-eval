# file: sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest
from sty.primitive import Register

class MockRegister(Register):
    def __init__(self, is_muted=False):
        self.is_muted = is_muted

    def eightbit_call(self, *args, **kwargs):
        return "eightbit"

    def rgb_call(self, *args, **kwargs):
        return "rgb"

    def __getattr__(self, name):
        return f"attr_{name}"

@pytest.fixture
def register():
    return MockRegister()

def test_call_muted(register):
    register.is_muted = True
    assert register() == ""

def test_call_eightbit(register):
    assert register(42) == "eightbit"

def test_call_attr(register):
    assert register("red") == "attr_red"

def test_call_rgb(register):
    assert register(102, 49, 42) == "rgb"

def test_call_empty(register):
    assert register(1, 2) == ""
