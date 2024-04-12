# file lib/ansible/modules/iptables.py:571-573
# lines [571, 572, 573]
# branches ['572->exit', '572->573']

import pytest
from ansible.modules.iptables import append_match

# Mocking the rule list to verify the append_match function behavior
@pytest.fixture
def mock_rule():
    return []

# Test function to check if the match is correctly appended to the rule
def test_append_match_with_param(mock_rule):
    # Call the function with a parameter
    append_match(mock_rule, param='some_param', match='tcp')
    # Assert that the rule list is correctly modified
    assert mock_rule == ['-m', 'tcp'], "The match was not appended correctly when param is provided"

# Test function to check that nothing is appended when param is None
def test_append_match_without_param(mock_rule):
    # Call the function with no parameter
    append_match(mock_rule, param=None, match='tcp')
    # Assert that the rule list remains unchanged
    assert mock_rule == [], "The rule list should not be modified when param is None"
