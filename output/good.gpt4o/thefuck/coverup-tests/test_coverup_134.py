# file thefuck/corrector.py:8-19
# lines []
# branches ['18->15']

import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from thefuck.corrector import get_loaded_rules, Rule

@pytest.fixture
def mock_rule(mocker):
    mock_rule = mocker.patch('thefuck.corrector.Rule')
    return mock_rule

def test_get_loaded_rules(mocker, mock_rule):
    # Create a mock Path object
    mock_path = mocker.MagicMock(spec=Path)
    mock_path.name = 'test_rule.py'
    mock_rule_instance = MagicMock(is_enabled=True)
    mock_rule.from_path.return_value = mock_rule_instance
    
    # Call the function with the mock path
    rules = list(get_loaded_rules([mock_path]))
    
    # Assertions to verify the postconditions
    assert len(rules) == 1
    assert rules[0] == mock_rule_instance
    assert rules[0].is_enabled

    # Clean up
    mock_rule.from_path.reset_mock()

def test_get_loaded_rules_with_disabled_rule(mocker, mock_rule):
    # Create a mock Path object
    mock_path = mocker.MagicMock(spec=Path)
    mock_path.name = 'test_rule.py'
    mock_rule_instance = MagicMock(is_enabled=False)
    mock_rule.from_path.return_value = mock_rule_instance
    
    # Call the function with the mock path
    rules = list(get_loaded_rules([mock_path]))
    
    # Assertions to verify the postconditions
    assert len(rules) == 0

    # Clean up
    mock_rule.from_path.reset_mock()

def test_get_loaded_rules_with_init_py(mocker, mock_rule):
    # Create a mock Path object for __init__.py
    mock_path = mocker.MagicMock(spec=Path)
    mock_path.name = '__init__.py'
    
    # Call the function with the mock path
    rules = list(get_loaded_rules([mock_path]))
    
    # Assertions to verify the postconditions
    assert len(rules) == 0

    # Clean up
    mock_rule.from_path.reset_mock()
