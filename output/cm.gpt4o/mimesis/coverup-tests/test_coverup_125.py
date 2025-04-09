# file mimesis/providers/path.py:51-59
# lines [51, 59]
# branches []

import pytest
from mimesis.providers.path import Path
from unittest.mock import patch

@pytest.fixture
def path_provider():
    return Path()

def test_home_path(path_provider):
    with patch.object(path_provider, '_pathlib_home', '/mock/home'):
        home_path = path_provider.home()
        assert home_path == '/mock/home'
