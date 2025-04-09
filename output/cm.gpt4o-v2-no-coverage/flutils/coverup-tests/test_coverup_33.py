# file: flutils/namedtupleutils.py:181-186
# asked: {"lines": [181, 182, 184, 186], "branches": []}
# gained: {"lines": [181, 182, 184, 186], "branches": []}

import pytest
from types import SimpleNamespace
from typing import NamedTuple
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_simplenamespace():
    class ExpectedNamedTuple(NamedTuple):
        a: int
        b: str

    obj = SimpleNamespace(a=1, b='test')
    result = _to_namedtuple(obj)
    
    assert isinstance(result, tuple)
    assert result.a == 1
    assert result.b == 'test'
    assert result == ExpectedNamedTuple(a=1, b='test')

def test_to_namedtuple_with_empty_simplenamespace():
    class ExpectedNamedTuple(NamedTuple):
        pass

    obj = SimpleNamespace()
    result = _to_namedtuple(obj)
    
    assert isinstance(result, tuple)
    assert result == ExpectedNamedTuple()

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
