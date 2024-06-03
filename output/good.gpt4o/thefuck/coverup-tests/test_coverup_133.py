# file thefuck/logs.py:75-81
# lines [76, 77, 78, 79, 80, 81]
# branches ['76->exit', '76->77']

import pytest
import sys
from unittest import mock
from thefuck import logs

@pytest.fixture
def mock_settings_debug_true(mocker):
    mocker.patch('thefuck.logs.settings', debug=True)

def test_debug_with_debug_enabled(mock_settings_debug_true, capsys):
    test_message = "Test debug message"
    logs.debug(test_message)
    captured = capsys.readouterr()
    assert "DEBUG:" in captured.err
    assert test_message in captured.err

@pytest.fixture
def mock_settings_debug_false(mocker):
    mocker.patch('thefuck.logs.settings', debug=False)

def test_debug_with_debug_disabled(mock_settings_debug_false, capsys):
    test_message = "Test debug message"
    logs.debug(test_message)
    captured = capsys.readouterr()
    assert captured.err == ""
