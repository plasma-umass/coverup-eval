# file thefuck/shells/generic.py:56-71
# lines [56, 58, 59, 60, 61, 63, 64, 65, 67, 68, 69, 70, 71]
# branches ['59->exit', '59->60', '64->65', '64->67', '67->exit', '67->68', '70->67', '70->71']

import os
import io
import pytest
from unittest import mock
from thefuck.shells.generic import Generic
from thefuck.conf import settings

@pytest.fixture
def mock_settings():
    original_history_limit = settings.history_limit
    settings.history_limit = 10
    yield
    settings.history_limit = original_history_limit

@pytest.fixture
def mock_history_file(tmp_path):
    history_file = tmp_path / "history_file"
    history_file.write_text("line1\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10\nline11\n", encoding='utf-8')
    return history_file

@pytest.fixture
def mock_generic(mocker, mock_history_file):
    mocker.patch('thefuck.shells.generic.Generic._get_history_file_name', return_value=str(mock_history_file))
    mocker.patch('thefuck.shells.generic.Generic._script_from_history', side_effect=lambda x: x)
    return Generic()

def test_get_history_lines(mock_generic, mock_settings):
    history_lines = list(mock_generic._get_history_lines())
    assert len(history_lines) == 10
    assert history_lines == ["line2", "line3", "line4", "line5", "line6", "line7", "line8", "line9", "line10", "line11"]
