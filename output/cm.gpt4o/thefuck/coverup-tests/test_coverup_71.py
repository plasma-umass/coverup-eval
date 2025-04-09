# file thefuck/logs.py:39-40
# lines [39, 40]
# branches []

import pytest
from unittest.mock import Mock, patch
from thefuck.logs import rule_failed

def test_rule_failed(mocker):
    # Mock the rule object and exc_info
    rule = Mock()
    rule.name = "test_rule"
    exc_info = Mock()

    # Patch the exception function to verify it is called correctly
    mock_exception = mocker.patch('thefuck.logs.exception')

    # Call the function under test
    rule_failed(rule, exc_info)

    # Assert that the exception function was called with the correct arguments
    mock_exception.assert_called_once_with(u'Rule test_rule', exc_info)
