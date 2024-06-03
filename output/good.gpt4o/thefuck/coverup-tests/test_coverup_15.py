# file thefuck/corrector.py:8-19
# lines [8, 15, 16, 17, 18, 19]
# branches ['15->exit', '15->16', '16->15', '16->17', '18->15', '18->19']

import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from thefuck.corrector import get_loaded_rules, Rule

@pytest.fixture
def mock_rule(mocker):
    mock_rule = mocker.patch('thefuck.corrector.Rule')
    mock_rule.from_path.side_effect = lambda path: MagicMock(is_enabled=True) if path.name != '__init__.py' else None
    return mock_rule

def test_get_loaded_rules(mock_rule):
    paths = [Path('rule1.py'), Path('rule2.py'), Path('__init__.py')]
    rules = list(get_loaded_rules(paths))
    
    assert len(rules) == 2
    assert all(isinstance(rule, MagicMock) for rule in rules)
    assert mock_rule.from_path.call_count == 2
    assert mock_rule.from_path.call_args_list[0][0][0].name == 'rule1.py'
    assert mock_rule.from_path.call_args_list[1][0][0].name == 'rule2.py'
