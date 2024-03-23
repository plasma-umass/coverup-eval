# file thefuck/types.py:111-120
# lines [111, 112, 113, 114, 115, 116, 117, 118, 120]
# branches ['112->113', '112->120']

import pytest
from thefuck.types import Rule

# Define a dummy side effect function for testing
def dummy_side_effect():
    pass

# Define a dummy match function for testing
def dummy_match(command):
    return True

# Define a dummy get_new_command function for testing
def dummy_get_new_command(command):
    return 'new_command'

@pytest.fixture
def rule():
    return Rule(name='test_rule',
                match=dummy_match,
                get_new_command=dummy_get_new_command,
                enabled_by_default=True,
                side_effect=dummy_side_effect,
                priority=1000,
                requires_output=True)

def test_rule_equality(rule):
    # Create another rule with the same properties
    same_rule = Rule(name='test_rule',
                     match=dummy_match,
                     get_new_command=dummy_get_new_command,
                     enabled_by_default=True,
                     side_effect=dummy_side_effect,
                     priority=1000,
                     requires_output=True)
    
    # Create a rule with different properties
    different_rule = Rule(name='different_rule',
                          match=dummy_match,
                          get_new_command=dummy_get_new_command,
                          enabled_by_default=False,
                          side_effect=dummy_side_effect,
                          priority=500,
                          requires_output=False)
    
    # Assert that the rule is equal to itself
    assert rule == rule
    
    # Assert that the rule is equal to another rule with the same properties
    assert rule == same_rule
    
    # Assert that the rule is not equal to a rule with different properties
    assert rule != different_rule
    
    # Assert that the rule is not equal to a non-Rule object
    assert rule != "not_a_rule_object"

# Run the test
def test_rule_inequality_with_non_rule_object(rule):
    non_rule_object = "I am not a rule"
    assert not (rule == non_rule_object)
