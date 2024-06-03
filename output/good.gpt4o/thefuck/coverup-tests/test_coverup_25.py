# file thefuck/types.py:217-223
# lines [217, 219, 220, 221, 223]
# branches ['219->220', '219->223']

import pytest
from thefuck.types import CorrectedCommand

@pytest.fixture
def corrected_command():
    return CorrectedCommand(script='echo test', side_effect=None, priority=0)

def test_corrected_command_eq_same_type(corrected_command, mocker):
    other = CorrectedCommand(script='echo test', side_effect=None, priority=0)
    assert corrected_command == other

def test_corrected_command_eq_different_type(corrected_command):
    assert corrected_command != "not a CorrectedCommand"

def test_corrected_command_eq_different_script(corrected_command):
    other = CorrectedCommand(script='echo different', side_effect=None, priority=0)
    assert corrected_command != other

def test_corrected_command_eq_different_side_effect(corrected_command):
    other = CorrectedCommand(script='echo test', side_effect='side effect 2', priority=0)
    assert corrected_command != other
