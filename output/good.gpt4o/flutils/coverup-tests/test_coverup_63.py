# file flutils/namedtupleutils.py:141-177
# lines [149, 150, 151, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 167, 168, 169]
# branches ['148->149', '154->155', '156->157', '156->169', '159->160', '159->163', '163->165', '163->169']

import pytest
from collections import namedtuple
from typing import NamedTuple, Sequence, Union, List, Any, Tuple, cast
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_sequence_type_error():
    with pytest.raises(TypeError, match="Can convert only 'list', 'tuple', 'dict' to a NamedTuple; got:"):
        _to_namedtuple("string", _started=False)

def test_to_namedtuple_namedtuple_conversion():
    TestNamedTuple = namedtuple('TestNamedTuple', 'a b')
    obj = TestNamedTuple(a=1, b=2)
    
    result = _to_namedtuple(obj)
    
    assert isinstance(result, tuple)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_namedtuple_empty_fields():
    TestNamedTuple = namedtuple('TestNamedTuple', '')
    obj = TestNamedTuple()
    
    result = _to_namedtuple(obj)
    
    assert isinstance(result, tuple)
    assert result == obj
