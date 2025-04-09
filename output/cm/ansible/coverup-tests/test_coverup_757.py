# file lib/ansible/playbook/conditional.py:42-50
# lines [42, 44, 49]
# branches []

import pytest
from ansible.playbook.conditional import Conditional

# Mocking the Base class since it's not provided in the snippet
class Base:
    def __init__(self):
        self._when = []

# Inheriting from Base as Conditional is supposed to be a mix-in
class TestConditional(Base, Conditional):
    pass

def test_conditional_when_attribute():
    # Create an instance of the TestConditional class
    conditional_instance = TestConditional()

    # Assert that the _when attribute starts as an empty list
    assert conditional_instance._when == []

    # Extend the _when list with new conditions
    conditional_instance._when.extend(['condition1', 'condition2'])

    # Assert that the _when attribute is correctly extended
    assert conditional_instance._when == ['condition1', 'condition2']

    # Prepend a new condition to the _when list
    conditional_instance._when = ['condition0'] + conditional_instance._when

    # Assert that the _when attribute is correctly prepended
    assert conditional_instance._when == ['condition0', 'condition1', 'condition2']

    # Clean up after the test
    del conditional_instance
