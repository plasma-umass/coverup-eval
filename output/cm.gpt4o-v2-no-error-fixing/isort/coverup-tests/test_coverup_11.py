# file: isort/exceptions.py:12-21
# asked: {"lines": [12, 13, 15, 16, 17, 21], "branches": []}
# gained: {"lines": [12, 13, 15, 16, 17, 21], "branches": []}

import pytest
from isort.exceptions import InvalidSettingsPath, ISortError

def test_invalid_settings_path():
    invalid_path = "/invalid/path"
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(invalid_path)
    
    assert str(exc_info.value) == (
        f"isort was told to use the settings_path: {invalid_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
    assert exc_info.value.settings_path == invalid_path
