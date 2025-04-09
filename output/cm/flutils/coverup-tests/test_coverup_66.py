# file flutils/namedtupleutils.py:141-177
# lines [169, 171, 172, 173, 174, 175, 176, 177]
# branches ['154->171', '156->169', '163->169', '172->173', '172->175', '175->176', '175->177']

import pytest
from collections import namedtuple
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_empty_namedtuple():
    # Create a namedtuple with no fields
    EmptyNamedTuple = namedtuple('EmptyNamedTuple', [])
    empty_namedtuple_instance = EmptyNamedTuple()

    # Call the function with the empty namedtuple instance
    result = _to_namedtuple(empty_namedtuple_instance)

    # Check that the result is the same instance (since it should not be converted)
    assert result == empty_namedtuple_instance
