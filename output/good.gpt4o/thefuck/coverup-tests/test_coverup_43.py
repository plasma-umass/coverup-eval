# file thefuck/corrector.py:40-49
# lines [40, 46, 47, 48, 49]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from thefuck.corrector import get_rules

@pytest.fixture
def mock_get_rules_import_paths(mocker):
    mock = mocker.patch('thefuck.corrector.get_rules_import_paths')
    mock.return_value = [Path('/fake/path1'), Path('/fake/path2')]
    return mock

@pytest.fixture
def mock_get_loaded_rules(mocker):
    mock = mocker.patch('thefuck.corrector.get_loaded_rules')
    mock.return_value = [
        MagicMock(priority=2),
        MagicMock(priority=1),
        MagicMock(priority=3)
    ]
    return mock

def test_get_rules(mock_get_rules_import_paths, mock_get_loaded_rules):
    rules = get_rules()
    assert len(rules) == 3
    assert rules[0].priority == 1
    assert rules[1].priority == 2
    assert rules[2].priority == 3
