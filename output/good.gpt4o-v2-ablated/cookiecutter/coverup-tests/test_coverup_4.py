# file: cookiecutter/repository.py:49-60
# asked: {"lines": [49, 55, 57, 58, 60], "branches": []}
# gained: {"lines": [49, 55, 57, 58, 60], "branches": []}

import os
import pytest

from cookiecutter.repository import repository_has_cookiecutter_json

@pytest.fixture
def temp_repo_dir(tmp_path):
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    yield repo_dir
    # Cleanup is handled by tmp_path fixture

def test_repository_has_cookiecutter_json_with_valid_repo(temp_repo_dir):
    cookiecutter_json_path = temp_repo_dir / "cookiecutter.json"
    cookiecutter_json_path.write_text("{}")
    
    assert repository_has_cookiecutter_json(str(temp_repo_dir)) is True

def test_repository_has_cookiecutter_json_without_cookiecutter_json(temp_repo_dir):
    assert repository_has_cookiecutter_json(str(temp_repo_dir)) is False

def test_repository_has_cookiecutter_json_with_invalid_repo():
    assert repository_has_cookiecutter_json("non_existent_directory") is False
