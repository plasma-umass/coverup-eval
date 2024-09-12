# file: f127/__init__.py:1-18
# asked: {"lines": [5, 7], "branches": [[4, 5], [6, 7]]}
# gained: {"lines": [5, 7], "branches": [[4, 5], [6, 7]]}

import pytest
from f127 import intersection

def test_intersection_prime_length():
    assert intersection((1, 10), (5, 15)) == "YES"  # Length is 5, which is prime

def test_intersection_non_prime_length():
    assert intersection((1, 10), (6, 15)) == "NO"  # Length is 4, which is not prime

def test_intersection_no_overlap():
    assert intersection((1, 5), (6, 10)) == "NO"  # No overlap

def test_intersection_edge_cases():
    assert intersection((0, 1), (0, 1)) == "NO"  # Length is 1, which is not prime
    assert intersection((0, 2), (0, 2)) == "YES"  # Length is 2, which is prime

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: nothing to setup
    yield
    # Teardown: nothing to teardown
