# file: cookiecutter/repository.py:49-60
# asked: {"lines": [49, 55, 57, 58, 60], "branches": []}
# gained: {"lines": [49, 55, 57, 58, 60], "branches": []}

import os
import pytest

from cookiecutter.repository import repository_has_cookiecutter_json

def test_repository_has_cookiecutter_json_valid_directory_with_config(monkeypatch, tmp_path):
    # Setup
    repo_dir = tmp_path / "valid_repo"
    repo_dir.mkdir()
    config_file = repo_dir / "cookiecutter.json"
    config_file.write_text("{}")

    # Test
    assert repository_has_cookiecutter_json(str(repo_dir)) is True

def test_repository_has_cookiecutter_json_valid_directory_without_config(monkeypatch, tmp_path):
    # Setup
    repo_dir = tmp_path / "valid_repo"
    repo_dir.mkdir()

    # Test
    assert repository_has_cookiecutter_json(str(repo_dir)) is False

def test_repository_has_cookiecutter_json_invalid_directory(monkeypatch):
    # Test
    assert repository_has_cookiecutter_json("non_existent_dir") is False
