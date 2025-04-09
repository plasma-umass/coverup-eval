# file mimesis/providers/path.py:61-71
# lines [69, 70, 71]
# branches []

import pytest
from mimesis.providers.path import Path
from unittest.mock import patch

@pytest.fixture
def path_provider():
    return Path()

def test_user_windows_platform(path_provider, mocker):
    mocker.patch.object(path_provider, 'platform', 'win32')
    mocker.patch.object(path_provider, 'random')
    path_provider.random.choice.return_value = 'oretha'
    
    result = path_provider.user()
    
    assert result == str(path_provider._pathlib_home / 'Oretha')

def test_user_non_windows_platform(path_provider, mocker):
    mocker.patch.object(path_provider, 'platform', 'linux')
    mocker.patch.object(path_provider, 'random')
    path_provider.random.choice.return_value = 'ORETHA'
    
    result = path_provider.user()
    
    assert result == str(path_provider._pathlib_home / 'oretha')
