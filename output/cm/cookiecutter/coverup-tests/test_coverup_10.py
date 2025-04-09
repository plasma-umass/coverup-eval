# file cookiecutter/repository.py:49-60
# lines [49, 55, 57, 58, 60]
# branches []

import os
import pytest
import shutil
from cookiecutter.repository import repository_has_cookiecutter_json

@pytest.fixture
def temp_repo_dir(tmp_path):
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    return repo_dir

def test_repository_has_cookiecutter_json_with_cookiecutter_file(temp_repo_dir):
    cookiecutter_file = temp_repo_dir / 'cookiecutter.json'
    cookiecutter_file.touch()  # Create an empty cookiecutter.json file

    assert repository_has_cookiecutter_json(str(temp_repo_dir)) is True

def test_repository_has_cookiecutter_json_without_cookiecutter_file(temp_repo_dir):
    assert repository_has_cookiecutter_json(str(temp_repo_dir)) is False

def test_repository_has_cookiecutter_json_with_nonexistent_directory():
    nonexistent_dir = '/path/to/nonexistent/directory'
    assert repository_has_cookiecutter_json(nonexistent_dir) is False
