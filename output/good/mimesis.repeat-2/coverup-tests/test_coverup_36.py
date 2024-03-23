# file mimesis/providers/path.py:23-34
# lines [23, 30, 31, 32, 33, 34]
# branches []

import pytest
import sys
from mimesis.providers import Path
from pathlib import PureWindowsPath, PurePosixPath

# Define a fixture to clean up the environment after the test
@pytest.fixture
def mock_sys_platform(mocker):
    original_platform = sys.platform
    yield
    sys.platform = original_platform

# Test function to cover missing branches for different platforms
@pytest.mark.parametrize("platform", ["linux", "darwin", "win32", "win64"])
def test_path_init_platforms(platform, mock_sys_platform, mocker):
    mocker.patch('sys.platform', platform)
    path_provider = Path(platform=platform)

    assert path_provider.platform == platform
    if 'win' in platform:
        assert isinstance(path_provider._pathlib_home, PureWindowsPath)
    else:
        assert isinstance(path_provider._pathlib_home, PurePosixPath)
