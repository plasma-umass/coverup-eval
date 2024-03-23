# file thefuck/corrector.py:8-19
# lines [8, 15, 16, 17, 18, 19]
# branches ['15->exit', '15->16', '16->15', '16->17', '18->15', '18->19']

import pytest
from thefuck.corrector import get_loaded_rules
from thefuck.types import Rule
from pathlib import Path
from unittest.mock import Mock


# Mock Rule class to control the behavior of from_path and is_enabled
class MockRule(Rule):
    def __init__(self, is_enabled):
        self._is_enabled = is_enabled

    @classmethod
    def from_path(cls, path):
        if path.name == 'mock_rule.py':
            return cls(is_enabled=True)
        elif path.name == 'disabled_rule.py':
            return cls(is_enabled=False)
        return None

    @property
    def is_enabled(self):
        return self._is_enabled


@pytest.fixture
def mock_rule(mocker):
    mocker.patch('thefuck.corrector.Rule', new=MockRule)


def test_get_loaded_rules_with_enabled_and_disabled_rules(mock_rule, tmp_path):
    # Create mock rule files
    enabled_rule_path = tmp_path / 'mock_rule.py'
    enabled_rule_path.touch()
    disabled_rule_path = tmp_path / 'disabled_rule.py'
    disabled_rule_path.touch()
    init_file_path = tmp_path / '__init__.py'
    init_file_path.touch()

    # Create a list of paths including the mock rule files and the __init__.py
    rules_paths = [enabled_rule_path, disabled_rule_path, init_file_path]

    # Convert to Path objects
    rules_paths = [Path(str(path)) for path in rules_paths]

    # Call the function and convert the result to a list to force generator evaluation
    rules = list(get_loaded_rules(rules_paths))

    # Assert that only the enabled rule is yielded
    assert len(rules) == 1
    assert isinstance(rules[0], MockRule)
    assert rules[0].is_enabled


def test_get_loaded_rules_with_no_rules(mock_rule, tmp_path):
    # Create an empty list of paths
    rules_paths = []

    # Call the function and convert the result to a list to force generator evaluation
    rules = list(get_loaded_rules(rules_paths))

    # Assert that no rules are yielded
    assert len(rules) == 0
