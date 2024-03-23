# file thefuck/conf.py:58-65
# lines [58, 60, 62, 63, 64, 65]
# branches ['63->64', '63->65']

import os
from pathlib import Path
from unittest.mock import patch
import pytest
from thefuck.conf import Settings

@pytest.fixture
def mock_user_dir(tmp_path):
    with patch.object(Settings, '_get_user_dir_path', return_value=tmp_path):
        yield tmp_path

def test_setup_user_dir_creates_directory(mock_user_dir):
    settings = Settings()
    rules_dir = mock_user_dir / 'rules'
    assert not rules_dir.exists()
    settings._setup_user_dir()
    assert rules_dir.is_dir()
    assert settings.user_dir == mock_user_dir

def test_setup_user_dir_existing_directory(mock_user_dir):
    settings = Settings()
    rules_dir = mock_user_dir / 'rules'
    rules_dir.mkdir(parents=True)
    assert rules_dir.exists()
    settings._setup_user_dir()
    assert rules_dir.is_dir()
    assert settings.user_dir == mock_user_dir
