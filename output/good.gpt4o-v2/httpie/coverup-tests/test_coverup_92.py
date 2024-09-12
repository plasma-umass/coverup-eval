# file: httpie/config.py:81-82
# asked: {"lines": [81, 82], "branches": []}
# gained: {"lines": [81, 82], "branches": []}

import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

def test_is_new_when_path_does_not_exist(monkeypatch):
    # Arrange
    path = Path('/non/existent/path')
    config = BaseConfigDict(path)

    # Act
    result = config.is_new()

    # Assert
    assert result is True

def test_is_new_when_path_exists(monkeypatch):
    # Arrange
    path = Path('/existent/path')
    config = BaseConfigDict(path)

    def mock_exists(self):
        return True

    # Mock the Path.exists method to return True
    monkeypatch.setattr(Path, 'exists', mock_exists)

    # Act
    result = config.is_new()

    # Assert
    assert result is False
