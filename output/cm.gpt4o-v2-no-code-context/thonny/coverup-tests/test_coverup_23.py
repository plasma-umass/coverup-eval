# file: thonny/jedi_utils.py:70-87
# asked: {"lines": [70, 71, 73, 74, 75, 76, 77, 78, 82, 83, 85, 87], "branches": [[73, 74], [73, 82], [83, 85], [83, 87]]}
# gained: {"lines": [70, 71, 73, 74, 75, 76, 77, 78, 82, 83, 87], "branches": [[73, 74], [73, 82], [83, 87]]}

import pytest
from unittest import mock
from thonny.jedi_utils import get_interpreter_completions

@pytest.fixture
def mock_jedi(mocker):
    mock_jedi = mocker.patch('thonny.jedi_utils.jedi', create=True)
    return mock_jedi

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('thonny.jedi_utils.logger')

def test_get_interpreter_completions_with_older_jedi_and_sys_path(mock_jedi, mock_logger, mocker):
    mock_jedi.Interpreter.side_effect = [Exception("test exception"), mock.Mock()]
    mock_jedi.Interpreter.return_value.completions = mock.Mock(return_value=[])
    mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=True)
    
    result = get_interpreter_completions("source", [{}], sys_path=["/some/path"])
    
    assert result == []
    mock_logger.info.assert_called_once_with("Could not get completions with given sys_path", exc_info=mock.ANY)

def test_get_interpreter_completions_with_older_jedi_no_sys_path(mock_jedi, mocker):
    mock_jedi.Interpreter.return_value.completions = mock.Mock(return_value=[])
    mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=True)
    
    result = get_interpreter_completions("source", [{}])
    
    assert result == []

def test_get_interpreter_completions_with_newer_jedi(mock_jedi, mocker):
    mock_jedi.Interpreter.return_value.complete = mock.Mock(return_value=[])
    mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=False)
    
    result = get_interpreter_completions("source", [{}])
    
    assert result == []
