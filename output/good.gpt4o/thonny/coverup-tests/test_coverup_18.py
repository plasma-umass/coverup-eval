# file thonny/plugins/pgzero_frontend.py:22-32
# lines [22, 23, 24, 25, 26, 27, 28, 29, 30, 32]
# branches []

import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_workbench(mocker):
    mock = mocker.patch('thonny.plugins.pgzero_frontend.get_workbench')
    return mock

def test_load_plugin(mock_workbench):
    from thonny.plugins.pgzero_frontend import load_plugin, _OPTION_NAME, update_environment

    # Mock the necessary methods and attributes
    mock_workbench_instance = mock_workbench.return_value
    mock_workbench_instance.set_default = MagicMock()
    mock_workbench_instance.add_command = MagicMock()
    mock_workbench_instance.toggle_variable = MagicMock()
    mock_update_environment = patch('thonny.plugins.pgzero_frontend.update_environment', MagicMock()).start()

    # Mock the toggle_variable function
    with patch('thonny.plugins.pgzero_frontend.toggle_variable', new=mock_workbench_instance.toggle_variable):
        # Call the function to test
        load_plugin()

        # Assertions to verify the expected behavior
        mock_workbench_instance.set_default.assert_called_once_with(_OPTION_NAME, False)
        mock_workbench_instance.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            "Pygame Zero mode",
            mock_workbench_instance.toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )
        mock_update_environment.assert_called_once()

    # Clean up
    patch.stopall()
