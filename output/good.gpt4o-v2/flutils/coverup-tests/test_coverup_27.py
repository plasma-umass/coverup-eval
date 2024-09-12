# file: flutils/namedtupleutils.py:181-186
# asked: {"lines": [181, 182, 184, 186], "branches": []}
# gained: {"lines": [181, 182, 184, 186], "branches": []}

import pytest
from types import SimpleNamespace
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_simplenamespace():
    # Create a SimpleNamespace object
    obj = SimpleNamespace(a=1, b=2)

    # Convert to NamedTuple
    result = _to_namedtuple(obj)

    # Verify the result is a NamedTuple with the same attributes
    assert result.a == 1
    assert result.b == 2
    assert isinstance(result, tuple)
    assert hasattr(result, '_fields')

