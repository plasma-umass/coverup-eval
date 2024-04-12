# file thonny/plugins/pgzero_frontend.py:9-12
# lines [10, 11, 12]
# branches []

import pytest
from unittest.mock import Mock, PropertyMock
from thonny.plugins.pgzero_frontend import toggle_variable

_OPTION_NAME = "run.pgzero_mode"

@pytest.fixture
def mock_workbench(mocker):
    workbench = mocker.Mock()
    variable = mocker.Mock()
    variable.get = mocker.Mock(return_value=True)
    variable.set = mocker.Mock()
    workbench.get_variable = mocker.Mock(return_value=variable)
    mocker.patch('thonny.plugins.pgzero_frontend.get_workbench', return_value=workbench)
    mocker.patch('thonny.plugins.pgzero_frontend.update_environment')
    return workbench, variable

def test_toggle_variable(mock_workbench):
    workbench, variable = mock_workbench
    # Precondition: The variable is initially True
    assert variable.get() is True
    
    # Action: Toggle the variable
    toggle_variable()
    
    # Postcondition: The variable should now be False
    variable.set.assert_called_once_with(False)
    workbench.get_variable.assert_called_once_with(_OPTION_NAME)
    assert variable.get.call_count == 2  # get is called twice, before and after set
