# file mimesis/providers/path.py:61-71
# lines [69, 70, 71]
# branches []

import pytest
from mimesis.providers import Path
from unittest.mock import patch
from pathlib import Path as pathlib_Path

@pytest.fixture
def path_provider():
    return Path()

def test_path_user_windows(path_provider):
    with patch.object(path_provider, 'platform', 'win32'):
        with patch.object(path_provider, '_pathlib_home', pathlib_Path('/home')):
            with patch.object(path_provider.random, 'choice', return_value='username'):
                user_path = path_provider.user()
                assert user_path == '/home/Username'
                assert user_path[1:].startswith('home/Username')

def test_path_user_unix(path_provider):
    with patch.object(path_provider, 'platform', 'linux'):
        with patch.object(path_provider, '_pathlib_home', pathlib_Path('/home')):
            with patch.object(path_provider.random, 'choice', return_value='username'):
                user_path = path_provider.user()
                assert user_path == '/home/username'
                assert user_path[1:].startswith('home/username')
