# file thonny/jedi_utils.py:90-96
# lines [91, 92, 94, 96]
# branches ['91->92', '91->94']

import pytest
from unittest.mock import MagicMock

def test_get_new_jedi_project_with_empty_sys_path():
    from thonny.jedi_utils import _get_new_jedi_project

    # Call the function with an empty sys_path
    result = _get_new_jedi_project([])

    # Assert that the result is None
    assert result is None

def test_get_new_jedi_project_with_non_empty_sys_path(mocker):
    from thonny.jedi_utils import _get_new_jedi_project
    import jedi

    # Mock jedi.Project to ensure it is not actually called
    mocked_project = mocker.patch.object(jedi, 'Project', autospec=True)

    # Call the function with a non-empty sys_path
    sys_path = ['/path/to/project']
    result = _get_new_jedi_project(sys_path)

    # Assert that jedi.Project was called with the correct arguments
    mocked_project.assert_called_once_with(path=sys_path[0], added_sys_path=sys_path)

    # Assert that the result is an instance of the mocked Project
    assert result == mocked_project.return_value
