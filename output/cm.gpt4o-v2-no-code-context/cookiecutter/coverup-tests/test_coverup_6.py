# file: cookiecutter/repository.py:49-60
# asked: {"lines": [49, 55, 57, 58, 60], "branches": []}
# gained: {"lines": [49, 55, 57, 58, 60], "branches": []}

import os
import pytest

from cookiecutter.repository import repository_has_cookiecutter_json

def test_repository_has_cookiecutter_json_with_valid_directory_and_file(tmp_path):
    # Create a temporary directory and a cookiecutter.json file inside it
    repo_directory = tmp_path / "repo"
    repo_directory.mkdir()
    cookiecutter_json = repo_directory / "cookiecutter.json"
    cookiecutter_json.write_text("{}")

    # Test that the function returns True
    assert repository_has_cookiecutter_json(str(repo_directory)) is True

def test_repository_has_cookiecutter_json_with_valid_directory_no_file(tmp_path):
    # Create a temporary directory without a cookiecutter.json file
    repo_directory = tmp_path / "repo"
    repo_directory.mkdir()

    # Test that the function returns False
    assert repository_has_cookiecutter_json(str(repo_directory)) is False

def test_repository_has_cookiecutter_json_with_no_directory(tmp_path):
    # Create a path that does not exist
    repo_directory = tmp_path / "non_existent_repo"

    # Test that the function returns False
    assert repository_has_cookiecutter_json(str(repo_directory)) is False
