# file lib/ansible/playbook/conditional.py:78-114
# lines [78, 87, 88, 89, 91, 92, 93, 96, 97, 98, 99, 101, 104, 105, 107, 108, 109, 111, 112, 114]
# branches ['88->89', '88->91', '93->96', '93->114', '96->97', '96->98', '98->99', '98->101', '104->105', '104->107', '108->93', '108->109']

import pytest
from ansible.errors import AnsibleError
from ansible.utils.display import Display

# Assuming the Conditional class is part of a module named conditional.py
# and the module ansible.playbook.conditional is accessible in the PYTHONPATH
from ansible.playbook.conditional import Conditional

# Mock the Display class to prevent actual output during testing
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'debug')

# Define a test class that includes the Conditional mixin
class TestConditional(Conditional):
    def __init__(self, when):
        self.when = when
        self._ds = {'example': 'datastructure'}

    def _check_conditional(self, conditional, templar, all_vars):
        # Mock the actual conditional check to return True or False based on a simple condition
        if conditional == 'true_condition':
            return True
        elif conditional == 'false_condition':
            return False
        else:
            raise Exception("Invalid conditional")

# Test function to improve coverage
def test_evaluate_conditional(mock_display):
    # Test with a list of conditionals that includes None, empty string, boolean, and string values
    conditionals = [None, '', True, 'true_condition', 'false_condition']
    test_obj = TestConditional(when=conditionals)

    # Mock objects for templar and all_vars
    templar = object()
    all_vars = {}

    # Call the method under test
    result = test_obj.evaluate_conditional(templar, all_vars)

    # Assert that the result is False, as 'false_condition' should cause the evaluation to fail
    assert not result

    # Test that an exception is raised when a conditional check fails
    with pytest.raises(AnsibleError) as excinfo:
        test_obj.when = ['invalid_condition']
        test_obj.evaluate_conditional(templar, all_vars)
    assert "The conditional check 'invalid_condition' failed." in str(excinfo.value)

# Clean up after the test
def teardown_function(function):
    # No global state was modified, so no teardown is required in this case
    pass
