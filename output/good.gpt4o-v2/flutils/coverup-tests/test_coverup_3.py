# file: flutils/namedtupleutils.py:93-103
# asked: {"lines": [93, 94, 96, 98, 99, 100, 101, 103], "branches": [[98, 99], [98, 103]]}
# gained: {"lines": [93, 94, 96, 98, 99, 100, 101, 103], "branches": [[98, 99], [98, 103]]}

import pytest
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_type_error():
    with pytest.raises(TypeError, match="Can convert only 'list', 'tuple', 'dict' to a NamedTuple; got:"):
        _to_namedtuple(42, _started=False)

def test_to_namedtuple_return_obj():
    obj = [1, 2, 3]
    assert _to_namedtuple(obj, _started=True) == obj
