# file pymonet/immutable_list.py:8-12
# lines [8, 9]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

@pytest.fixture
def immutable_list():
    return ImmutableList()

def test_immutable_list_instance(immutable_list):
    assert isinstance(immutable_list, ImmutableList), "The instance should be of type ImmutableList"
