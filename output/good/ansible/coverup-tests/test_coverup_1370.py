# file lib/ansible/playbook/conditional.py:62-64
# lines [63, 64]
# branches ['63->exit', '63->64']

import pytest
from ansible.playbook.conditional import Conditional
from unittest.mock import MagicMock

class TestConditional:
    @pytest.fixture
    def conditional(self):
        mock_loader = MagicMock()
        # Create a Conditional instance with a mock loader and a 'when' attribute
        conditional = Conditional(loader=mock_loader)
        conditional.when = None  # Initialize 'when' attribute
        return conditional

    def test_validate_when_with_non_list_value(self, conditional):
        non_list_value = 'some_condition'
        conditional._validate_when('when', 'when', non_list_value)
        assert getattr(conditional, 'when') == [non_list_value]

    def test_validate_when_with_list_value(self, conditional):
        list_value = ['some_condition']
        # Set the 'when' attribute to the list value before calling the method
        conditional.when = list_value
        conditional._validate_when('when', 'when', list_value)
        assert getattr(conditional, 'when') == list_value
