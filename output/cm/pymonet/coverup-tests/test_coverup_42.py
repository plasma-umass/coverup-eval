# file pymonet/immutable_list.py:132-150
# lines [132, 141, 142, 144, 145, 147, 148, 150]
# branches ['141->142', '141->144', '144->145', '144->147', '147->148', '147->150']

import pytest
from pymonet.immutable_list import ImmutableList

def test_find_with_tail():
    # Test when head does not satisfy the condition but tail does
    def condition(value):
        return value == "tail"

    immutable_list = ImmutableList("head", ImmutableList("tail", None))

    assert immutable_list.find(condition) == "tail"

def test_find_with_none_tail():
    # Test when neither head nor tail satisfy the condition
    def condition(value):
        return value == "nonexistent"

    immutable_list = ImmutableList("head", None)

    assert immutable_list.find(condition) is None
