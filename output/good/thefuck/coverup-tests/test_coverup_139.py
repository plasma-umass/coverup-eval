# file thefuck/rules/scm_correction.py:22-27
# lines [24, 25, 27]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.scm_correction import match, _get_actual_scm
from thefuck.rules.scm_correction import wrong_scm_patterns
from unittest.mock import Mock

@pytest.fixture
def mock_get_actual_scm(mocker):
    mock = mocker.patch('thefuck.rules.scm_correction._get_actual_scm', return_value=True)
    return mock

@pytest.fixture
def command_factory():
    def _factory(script, output):
        return Command(script, output)
    return _factory

def test_match_with_wrong_scm_pattern_and_correct_output(mock_get_actual_scm, command_factory):
    for scm, pattern in wrong_scm_patterns.items():
        command = command_factory(scm, pattern)
        assert match(command)
        mock_get_actual_scm.assert_called_once_with()
        mock_get_actual_scm.reset_mock()
