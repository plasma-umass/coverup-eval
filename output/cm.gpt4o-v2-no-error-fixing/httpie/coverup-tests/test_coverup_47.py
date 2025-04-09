# file: httpie/config.py:81-82
# asked: {"lines": [81, 82], "branches": []}
# gained: {"lines": [81, 82], "branches": []}

import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

@pytest.fixture
def temp_path(tmp_path):
    return tmp_path / "config.json"

def test_is_new_when_path_does_not_exist(temp_path):
    config = BaseConfigDict(temp_path)
    assert config.is_new() is True

def test_is_new_when_path_exists(temp_path):
    temp_path.touch()  # Create the file
    config = BaseConfigDict(temp_path)
    assert config.is_new() is False
