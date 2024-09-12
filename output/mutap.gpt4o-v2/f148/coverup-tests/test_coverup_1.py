# file: f148/__init__.py:1-11
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [8, 9], [8, 11]]}

import pytest
from f148 import bf

def test_bf_invalid_planets():
    assert bf("Pluto", "Earth") == ()
    assert bf("Earth", "Pluto") == ()
    assert bf("Pluto", "Pluto") == ()
    assert bf("Earth", "Earth") == ()

def test_bf_valid_planets():
    assert bf("Mercury", "Earth") == ("Venus",)
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Earth", "Jupiter") == ("Mars",)
    assert bf("Jupiter", "Earth") == ("Mars",)
    assert bf("Venus", "Neptune") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: nothing to setup
    yield
    # Teardown: nothing to teardown
