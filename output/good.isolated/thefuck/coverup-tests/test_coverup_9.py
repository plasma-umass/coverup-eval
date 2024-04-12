# file thefuck/types.py:89-109
# lines [89, 103, 104, 105, 106, 107, 108, 109]
# branches []

import pytest
from thefuck.types import Rule

def test_rule_initialization(mocker):
    # Mocking the functions that will be passed to the Rule constructor
    mock_match = mocker.Mock(return_value=True)
    mock_get_new_command = mocker.Mock(return_value="new_command")
    mock_side_effect = mocker.Mock()

    # Creating an instance of Rule with the mocked functions
    rule = Rule(
        name="test_rule",
        match=mock_match,
        get_new_command=mock_get_new_command,
        enabled_by_default=True,
        side_effect=mock_side_effect,
        priority=100,
        requires_output=True
    )

    # Asserting that the Rule instance has the correct attributes
    assert rule.name == "test_rule"
    assert rule.match is mock_match
    assert rule.get_new_command is mock_get_new_command
    assert rule.enabled_by_default is True
    assert rule.side_effect is mock_side_effect
    assert rule.priority == 100
    assert rule.requires_output is True

    # Cleanup is not necessary as we are using mocks and not modifying any global state
