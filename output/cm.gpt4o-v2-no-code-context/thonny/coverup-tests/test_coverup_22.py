# file: thonny/jedi_utils.py:90-96
# asked: {"lines": [90, 91, 92, 94, 96], "branches": [[91, 92], [91, 94]]}
# gained: {"lines": [90, 91, 92, 94, 96], "branches": [[91, 92], [91, 94]]}

import pytest
from unittest import mock
import sys

# Assuming the function _get_new_jedi_project is imported from thonny.jedi_utils
from thonny.jedi_utils import _get_new_jedi_project

def test_get_new_jedi_project_empty_sys_path():
    result = _get_new_jedi_project([])
    assert result is None

def test_get_new_jedi_project_with_sys_path(monkeypatch):
    mock_jedi = mock.Mock()
    monkeypatch.setitem(sys.modules, 'jedi', mock_jedi)
    
    sys_path = ["/some/path"]
    result = _get_new_jedi_project(sys_path)
    
    mock_jedi.Project.assert_called_once_with(path=sys_path[0], added_sys_path=sys_path)
    assert result == mock_jedi.Project.return_value
