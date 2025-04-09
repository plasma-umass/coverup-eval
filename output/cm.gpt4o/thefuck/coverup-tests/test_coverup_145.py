# file thefuck/shells/generic.py:56-71
# lines []
# branches ['59->exit', '64->67', '70->67']

import os
import io
import pytest
from unittest import mock
from thefuck.shells.generic import Generic
from thefuck.conf import settings

@pytest.fixture
def mock_settings(mocker):
    original_history_limit = settings.history_limit
    mocker.patch('thefuck.shells.generic.settings')
    settings.history_limit = 2
    yield
    settings.history_limit = original_history_limit

@pytest.fixture
def mock_history_file(mocker):
    history_content = "line1\nline2\nline3\n"
    mock_open = mocker.patch('io.open', mock.mock_open(read_data=history_content))
    yield mock_open

@pytest.fixture
def mock_isfile(mocker):
    mock_isfile = mocker.patch('os.path.isfile', return_value=True)
    yield mock_isfile

@pytest.fixture
def generic_instance():
    return Generic()

def test_get_history_lines_with_file(mock_settings, mock_history_file, mock_isfile, generic_instance):
    history_lines = list(generic_instance._get_history_lines())
    
    assert mock_isfile.called
    mock_history_file.assert_called_once_with(mock.ANY, 'r', encoding='utf-8', errors='ignore')
    
    assert len(history_lines) == 2
    assert history_lines == ['line2', 'line3']

def test_get_history_lines_no_file(mocker, generic_instance):
    mocker.patch('os.path.isfile', return_value=False)
    history_lines = list(generic_instance._get_history_lines())
    
    assert history_lines == []

def test_get_history_lines_no_limit(mocker, generic_instance):
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('io.open', mock.mock_open(read_data="line1\nline2\nline3\n"))
    mocker.patch('thefuck.shells.generic.settings', history_limit=None)
    
    history_lines = list(generic_instance._get_history_lines())
    
    assert len(history_lines) == 3
    assert history_lines == ['line1', 'line2', 'line3']
