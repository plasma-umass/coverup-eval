# file: thonny/jedi_utils.py:90-96
# asked: {"lines": [90, 91, 92, 94, 96], "branches": [[91, 92], [91, 94]]}
# gained: {"lines": [90, 91, 92, 94, 96], "branches": [[91, 92], [91, 94]]}

import pytest
from unittest import mock

def test_get_new_jedi_project_with_empty_sys_path():
    from thonny.jedi_utils import _get_new_jedi_project
    assert _get_new_jedi_project([]) is None

def test_get_new_jedi_project_with_non_empty_sys_path():
    from thonny.jedi_utils import _get_new_jedi_project
    with mock.patch('jedi.Project') as MockProject:
        sys_path = ['/some/path']
        project_instance = MockProject.return_value
        result = _get_new_jedi_project(sys_path)
        MockProject.assert_called_once_with(path=sys_path[0], added_sys_path=sys_path)
        assert result == project_instance
