# file thefuck/rules/aws_cli.py:9-11
# lines [9, 10, 11]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.aws_cli import match

@pytest.fixture
def aws_error_output():
    return "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run: aws help <command> <subcommand>\nmaybe you meant:"

@pytest.fixture
def non_aws_error_output():
    return "some random error message"

def test_match_with_aws_error(mocker, aws_error_output):
    command = Command('aws s3 ls', aws_error_output)
    assert match(command)

def test_match_without_aws_error(mocker, non_aws_error_output):
    command = Command('aws s3 ls', non_aws_error_output)
    assert not match(command)

def test_match_with_non_aws_command(mocker, aws_error_output):
    command = Command('not_aws_command', aws_error_output)
    assert not match(command)
