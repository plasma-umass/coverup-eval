# file flutils/namedtupleutils.py:93-103
# lines [93, 94, 96, 98, 99, 100, 101, 103]
# branches ['98->99', '98->103']

import pytest
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_type_error():
    with pytest.raises(TypeError) as excinfo:
        _to_namedtuple(42)
    assert "Can convert only 'list', 'tuple', 'dict' to a NamedTuple" in str(excinfo.value)
