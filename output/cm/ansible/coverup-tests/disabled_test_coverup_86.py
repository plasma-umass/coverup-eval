# file lib/ansible/galaxy/api.py:145-177
# lines [145, 146, 148, 150, 151, 152, 153, 155, 156, 157, 158, 159, 161, 162, 164, 165, 166, 167, 169, 170, 171, 174, 175, 177]
# branches ['150->151', '150->155', '156->157', '156->161', '169->170', '169->177']

import json
import os
import pytest
import stat
from unittest.mock import MagicMock

# Assuming the presence of the following within the ansible.galaxy.api module
from ansible.galaxy.api import _load_cache
from ansible.utils.display import Display

# Mock the Display class to capture output
@pytest.fixture
def mock_display(mocker):
    display_mock = mocker.patch.object(Display, 'vvvv')
    warning_mock = mocker.patch.object(Display, 'warning')
    return display_mock, warning_mock

# Test function to cover missing branches
def test_load_cache_world_writable(tmp_path, mock_display):
    cache_file = tmp_path / "galaxy_cache.json"
    cache_file.touch()
    cache_file.chmod(0o666)  # Make the file world writable

    # Call the function with the world writable cache file
    result = _load_cache(str(cache_file))

    # Assert that the result is None due to world writable permissions
    assert result is None

    # Assert that the warning was displayed
    _, warning_mock = mock_display
    warning_mock.assert_called_once_with(
        "Galaxy cache has world writable access (%s), ignoring it as a cache source." % str(cache_file)
    )

    # Clean up
    cache_file.unlink()

def test_load_cache_invalid_version(tmp_path, mock_display):
    cache_file = tmp_path / "galaxy_cache.json"
    cache_file.write_text(json.dumps({'version': 999}))  # Write invalid version to cache
    cache_file.chmod(0o600)  # Ensure the file is not world writable

    # Call the function with the invalid version cache file
    result = _load_cache(str(cache_file))

    # Assert that the cache is reset to the correct version
    assert result == {'version': 1}

    # Assert that the vvvv message was displayed
    display_mock, _ = mock_display
    display_mock.assert_called_with(
        "Galaxy cache file at '%s' has an invalid version, clearing" % str(cache_file)
    )

    # Clean up
    cache_file.unlink()

def test_load_cache_valid(tmp_path, mock_display):
    cache_file = tmp_path / "galaxy_cache.json"
    cache_data = {'version': 1, 'data': 'test'}
    cache_file.write_text(json.dumps(cache_data))  # Write valid cache data
    cache_file.chmod(0o600)  # Ensure the file is not world writable

    # Call the function with the valid cache file
    result = _load_cache(str(cache_file))

    # Assert that the cache is loaded correctly
    assert result == cache_data

    # Clean up
    cache_file.unlink()
