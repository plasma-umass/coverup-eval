# file flutils/namedtupleutils.py:181-186
# lines [181, 182, 184, 186]
# branches []

import pytest
from collections import namedtuple
from types import SimpleNamespace
from flutils.namedtupleutils import _to_namedtuple

# Define a namedtuple for testing purposes
TestNamedTuple = namedtuple('TestNamedTuple', 'field1 field2')

@pytest.fixture
def simple_namespace():
    # Create a SimpleNamespace object to be used in the test
    return SimpleNamespace(field1='value1', field2='value2')

def test_to_namedtuple_with_simplenamespace(simple_namespace):
    # Convert the SimpleNamespace to a namedtuple using the _to_namedtuple function
    result = _to_namedtuple(simple_namespace)
    
    # Check that the result is an instance of a namedtuple
    assert isinstance(result, tuple)
    assert hasattr(result, '_fields')
    
    # Check that the fields and values match those of the original SimpleNamespace
    assert result.field1 == simple_namespace.field1
    assert result.field2 == simple_namespace.field2

# Clean up is not necessary as the test does not modify any global state
