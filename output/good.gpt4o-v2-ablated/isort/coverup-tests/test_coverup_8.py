# file: isort/exceptions.py:12-21
# asked: {"lines": [12, 13, 15, 16, 17, 21], "branches": []}
# gained: {"lines": [12, 13, 15, 16, 17, 21], "branches": []}

import pytest
from isort.exceptions import InvalidSettingsPath

def test_invalid_settings_path():
    invalid_path = "/invalid/path"
    exception = InvalidSettingsPath(invalid_path)
    
    assert isinstance(exception, InvalidSettingsPath)
    assert exception.settings_path == invalid_path
    assert str(exception) == (
        f"isort was told to use the settings_path: {invalid_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
