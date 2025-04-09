# file: thonny/jedi_utils.py:52-67
# asked: {"lines": [52, 53, 55, 56, 57, 58, 59, 60, 62, 64, 65, 67], "branches": [[55, 56], [55, 64]]}
# gained: {"lines": [52, 53, 55, 56, 57, 58, 59, 60, 62, 64, 65, 67], "branches": [[55, 56], [55, 64]]}

import pytest
from unittest.mock import patch, MagicMock
import jedi
from thonny.jedi_utils import get_script_completions

# Mocking the logger to avoid actual logging during tests
@pytest.fixture
def mock_logger(monkeypatch):
    mock_logger = MagicMock()
    monkeypatch.setattr("thonny.jedi_utils.logger", mock_logger)
    return mock_logger

def test_get_script_completions_with_older_jedi(mock_logger):
    source = "import os\nos."
    row = 2
    column = 3
    filename = "test.py"
    sys_path = None

    with patch("thonny.jedi_utils._using_older_jedi", return_value=True), \
         patch("jedi.Script") as mock_script, \
         patch("thonny.jedi_utils._tweak_completions", return_value=["completion"]):
        
        mock_script_instance = mock_script.return_value
        mock_script_instance.completions.return_value = ["completion"]
        
        completions = get_script_completions(source, row, column, filename, sys_path)
        
        mock_script.assert_called_with(source, row, column, filename, sys_path=sys_path)
        mock_script_instance.completions.assert_called_once()
        assert completions == ["completion"]

def test_get_script_completions_with_newer_jedi(mock_logger):
    source = "import os\nos."
    row = 2
    column = 3
    filename = "test.py"
    sys_path = None

    with patch("thonny.jedi_utils._using_older_jedi", return_value=False), \
         patch("thonny.jedi_utils._get_new_jedi_project", return_value="project"), \
         patch("jedi.Script") as mock_script, \
         patch("thonny.jedi_utils._tweak_completions", return_value=["completion"]):
        
        mock_script_instance = mock_script.return_value
        mock_script_instance.complete.return_value = ["completion"]
        
        completions = get_script_completions(source, row, column, filename, sys_path)
        
        mock_script.assert_called_with(code=source, path=filename, project="project")
        mock_script_instance.complete.assert_called_with(line=row, column=column)
        assert completions == ["completion"]

def test_get_script_completions_with_exception(mock_logger):
    source = "import os\nos."
    row = 2
    column = 3
    filename = "test.py"
    sys_path = ["some_path"]

    with patch("thonny.jedi_utils._using_older_jedi", return_value=True), \
         patch("jedi.Script", side_effect=[Exception("test exception"), MagicMock()]) as mock_script, \
         patch("thonny.jedi_utils._tweak_completions", return_value=["completion"]):
        
        completions = get_script_completions(source, row, column, filename, sys_path)
        
        assert mock_logger.info.called
        assert mock_script.call_count == 2
        mock_script.assert_called_with(source, row, column, filename)
        assert completions == ["completion"]
