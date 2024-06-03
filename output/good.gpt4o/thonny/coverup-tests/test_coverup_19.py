# file thonny/jedi_utils.py:52-67
# lines [52, 53, 55, 56, 57, 58, 59, 60, 62, 64, 65, 67]
# branches ['55->56', '55->64']

import pytest
from unittest import mock
from thonny.jedi_utils import get_script_completions

def test_get_script_completions_with_sys_path(mocker):
    mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=True)
    mocker.patch('thonny.jedi_utils._tweak_completions', return_value='tweaked_completions')
    mock_logger = mocker.patch('thonny.jedi_utils.logger')
    
    mock_script = mocker.patch('jedi.Script')
    mock_script.return_value.completions.return_value = 'completions'
    
    source = "import os"
    row = 1
    column = 1
    filename = "test.py"
    sys_path = ["some_path"]
    
    result = get_script_completions(source, row, column, filename, sys_path)
    
    mock_script.assert_called_with(source, row, column, filename, sys_path=sys_path)
    assert result == 'tweaked_completions'
    mock_logger.info.assert_not_called()

def test_get_script_completions_without_sys_path(mocker):
    mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=True)
    mocker.patch('thonny.jedi_utils._tweak_completions', return_value='tweaked_completions')
    mock_logger = mocker.patch('thonny.jedi_utils.logger')
    
    mock_script = mocker.patch('jedi.Script')
    mock_script.side_effect = [Exception("error"), mock.Mock(completions=mock.Mock(return_value='completions'))]
    
    source = "import os"
    row = 1
    column = 1
    filename = "test.py"
    sys_path = ["some_path"]
    
    result = get_script_completions(source, row, column, filename, sys_path)
    
    assert mock_script.call_count == 2
    assert mock_script.call_args_list[0] == mock.call(source, row, column, filename, sys_path=sys_path)
    assert mock_script.call_args_list[1] == mock.call(source, row, column, filename)
    assert result == 'tweaked_completions'
    mock_logger.info.assert_called_once_with("Could not get completions with given sys_path", exc_info=mock.ANY)

def test_get_script_completions_new_jedi(mocker):
    mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=False)
    mocker.patch('thonny.jedi_utils._tweak_completions', return_value='tweaked_completions')
    mocker.patch('thonny.jedi_utils._get_new_jedi_project', return_value='project')
    
    mock_script = mocker.patch('jedi.Script')
    mock_script.return_value.complete.return_value = 'completions'
    
    source = "import os"
    row = 1
    column = 1
    filename = "test.py"
    sys_path = ["some_path"]
    
    result = get_script_completions(source, row, column, filename, sys_path)
    
    mock_script.assert_called_with(code=source, path=filename, project='project')
    assert result == 'tweaked_completions'
