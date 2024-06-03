# file thonny/jedi_utils.py:70-87
# lines [71, 73, 74, 75, 76, 77, 78, 82, 83, 85, 87]
# branches ['73->74', '73->82', '83->85', '83->87']

import pytest
from thonny.jedi_utils import get_interpreter_completions
import jedi
import logging

logger = logging.getLogger("thonny.jedi_utils")

@pytest.fixture
def mock_jedi_import(mocker):
    original_import = __import__

    def import_mock(name, *args):
        if name == "jedi":
            return jedi
        return original_import(name, *args)

    mocker.patch("builtins.__import__", side_effect=import_mock)
    return jedi

def test_get_interpreter_completions_with_older_jedi(mocker, mock_jedi_import):
    mocker.patch("thonny.jedi_utils._using_older_jedi", return_value=True)
    mocker.patch("thonny.jedi_utils._tweak_completions", return_value="mocked_completions")
    
    # Mocking the Interpreter to raise an exception first
    mock_interpreter = mocker.Mock()
    mock_interpreter.side_effect = [Exception("mocked exception"), mock_interpreter]
    mock_jedi_import.Interpreter = mock_interpreter
    
    source = "import os"
    namespaces = [{}]
    sys_path = ["mocked_path"]
    
    result = get_interpreter_completions(source, namespaces, sys_path)
    
    assert result == "mocked_completions"
    assert mock_interpreter.call_count == 2
    assert mock_interpreter.call_args_list[0] == mocker.call(source, namespaces, sys_path=sys_path)
    assert mock_interpreter.call_args_list[1] == mocker.call(source, namespaces)

def test_get_interpreter_completions_with_newer_jedi(mocker, mock_jedi_import):
    mocker.patch("thonny.jedi_utils._using_older_jedi", return_value=False)
    mocker.patch("thonny.jedi_utils._tweak_completions", return_value="mocked_completions")
    
    mock_interpreter = mocker.Mock()
    mock_jedi_import.Interpreter = mock_interpreter
    
    source = "import os"
    namespaces = [{}]
    
    result = get_interpreter_completions(source, namespaces)
    
    assert result == "mocked_completions"
    assert mock_interpreter.call_count == 1
    assert mock_interpreter.call_args == mocker.call(source, namespaces)
