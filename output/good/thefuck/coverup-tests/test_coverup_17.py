# file thefuck/types.py:217-223
# lines [217, 219, 220, 221, 223]
# branches ['219->220', '219->223']

import pytest
from thefuck.types import CorrectedCommand

@pytest.fixture
def corrected_command():
    return CorrectedCommand('ls', None, 100)

@pytest.fixture
def another_corrected_command():
    return CorrectedCommand('ls', None, 200)

@pytest.fixture
def different_corrected_command():
    return CorrectedCommand('rm -rf /', None, 100)

def test_corrected_command_equality(corrected_command, another_corrected_command):
    assert corrected_command == another_corrected_command

def test_corrected_command_inequality(corrected_command, different_corrected_command):
    assert corrected_command != different_corrected_command

def test_corrected_command_equality_with_non_corrected_command(corrected_command):
    assert corrected_command != 'ls'
