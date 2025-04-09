# file thefuck/rules/scm_correction.py:30-32
# lines [30, 31, 32]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.scm_correction import get_new_command

@pytest.fixture
def mock_get_actual_scm(mocker):
    return mocker.patch('thefuck.rules.scm_correction._get_actual_scm')

def test_get_new_command(mock_get_actual_scm):
    mock_get_actual_scm.return_value = 'git'
    command = Command('hg commit', '')
    new_command = get_new_command(command)
    assert new_command == 'git commit'
