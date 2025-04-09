# file thefuck/rules/aws_cli.py:9-11
# lines [9, 10, 11]
# branches []

import pytest
from thefuck.rules.aws_cli import match
from thefuck.types import Command

@pytest.fixture
def mock_command():
    return Command('aws s3 ls', 'usage: aws [options] [command] [parameters]\n\nmaybe you meant:\n\n  s3 ls\n')

def test_match(mock_command):
    assert match(mock_command)

def test_no_match():
    command = Command('aws s3 ls', 'some other output')
    assert not match(command)
