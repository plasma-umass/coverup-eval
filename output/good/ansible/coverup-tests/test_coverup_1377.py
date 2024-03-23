# file lib/ansible/playbook/conditional.py:78-114
# lines []
# branches ['88->91', '93->114', '104->107']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional
from ansible.template import Templar
from ansible.utils.display import Display

# Mock the display object to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'debug')

# Define a subclass of Conditional for testing purposes
class TestConditional(Conditional):
    def __init__(self, when):
        self.when = when
        self._ds = {'example': 'datastructure'}

    def _check_conditional(self, conditional, templar, all_vars):
        # Mock the actual conditional check to force different code paths
        if conditional == 'error':
            raise Exception("simulated error")
        return conditional == 'true'

# Test function to cover missing branches
def test_evaluate_conditional(mock_display):
    templar = Templar(loader=None, variables={})
    all_vars = {}

    # Test branch 88->91 (has _ds attribute)
    conditional_with_ds = TestConditional(when=['true'])
    assert conditional_with_ds.evaluate_conditional(templar, all_vars) is True

    # Test branch 93->114 (exception handling)
    conditional_with_error = TestConditional(when=['error'])
    with pytest.raises(AnsibleError):
        conditional_with_error.evaluate_conditional(templar, all_vars)

    # Test branch 104->107 (result changes from True to False)
    conditional_with_mixed = TestConditional(when=['true', 'false'])
    assert conditional_with_mixed.evaluate_conditional(templar, all_vars) is False
