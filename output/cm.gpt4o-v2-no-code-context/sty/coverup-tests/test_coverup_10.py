# file: sty/primitive.py:93-120
# asked: {"lines": [93, 99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [93, 99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest
from sty.primitive import Register

@pytest.fixture
def register():
    class TestRegister(Register):
        red = 'red_color'
    return TestRegister()

def test_register_call_muted(register, monkeypatch):
    monkeypatch.setattr(register, 'is_muted', True)
    assert register(42) == ""
    assert register('red') == ""
    assert register(102, 49, 42) == ""

def test_register_call_eightbit(register, monkeypatch):
    monkeypatch.setattr(register, 'is_muted', False)
    monkeypatch.setattr(register, 'eightbit_call', lambda *args, **kwargs: "eightbit")
    assert register(42) == "eightbit"

def test_register_call_string(register, monkeypatch):
    monkeypatch.setattr(register, 'is_muted', False)
    assert register('red') == 'red_color'

def test_register_call_rgb(register, monkeypatch):
    monkeypatch.setattr(register, 'is_muted', False)
    monkeypatch.setattr(register, 'rgb_call', lambda *args, **kwargs: "rgb")
    assert register(102, 49, 42) == "rgb"

def test_register_call_default(register, monkeypatch):
    monkeypatch.setattr(register, 'is_muted', False)
    assert register() == ""
    assert register(1, 2) == ""
    assert register(1, 2, 3, 4) == ""
