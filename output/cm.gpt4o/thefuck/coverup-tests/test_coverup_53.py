# file thefuck/types.py:48-52
# lines [48, 49, 50, 52]
# branches ['49->50', '49->52']

import pytest
from thefuck.types import Command

@pytest.fixture
def command():
    return Command("echo 'Hello, World!'", "Hello, World!")

def test_command_eq_same_type(command):
    other_command = Command("echo 'Hello, World!'", "Hello, World!")
    assert command == other_command

def test_command_eq_different_type(command):
    assert command != "Not a Command object"

def test_command_eq_different_script(command):
    other_command = Command("echo 'Goodbye, World!'", "Hello, World!")
    assert command != other_command

def test_command_eq_different_output(command):
    other_command = Command("echo 'Hello, World!'", "Goodbye, World!")
    assert command != other_command
