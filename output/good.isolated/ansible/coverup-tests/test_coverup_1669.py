# file lib/ansible/galaxy/token.py:123-140
# lines [137, 138]
# branches ['125->131', '136->137']

import os
import pytest
from ansible.galaxy.token import GalaxyToken
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'vvv')

# Test function to cover missing lines/branches
def test_galaxy_token_read_non_dict_content(tmp_path, mock_display, mocker):
    # Create a temporary token file with invalid content (not a dict)
    token_file = tmp_path / "token.yml"
    token_file.write_text("invalid_yaml_content")

    # Mock the yaml_load function to return non-dict content
    mocker.patch('ansible.galaxy.token.yaml_load', return_value="invalid_yaml_content")

    # Create a GalaxyToken instance with the path to the temporary token file
    token = GalaxyToken()
    token.b_file = str(token_file)  # Set the b_file attribute directly

    # Call the _read method and assert the result is an empty dict
    result = token._read()
    assert result == {}

    # Assert that the display method was called with the expected message
    Display.vvv.assert_called_with('Galaxy token file %s malformed, unable to read it' % token.b_file)

    # Clean up the temporary token file
    token_file.unlink()
