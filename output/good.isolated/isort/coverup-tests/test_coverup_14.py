# file isort/exceptions.py:12-21
# lines [12, 13, 15, 16, 17, 21]
# branches []

import pytest
from isort.exceptions import InvalidSettingsPath

def test_invalid_settings_path_exception():
    settings_path = "nonexistent_path"
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(settings_path)
    assert str(exc_info.value) == (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
    assert exc_info.value.settings_path == settings_path
