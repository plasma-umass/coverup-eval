# file cookiecutter/repository.py:49-60
# lines [49, 55, 57, 58, 60]
# branches []

import os
import pytest
from cookiecutter.repository import repository_has_cookiecutter_json

def test_repository_has_cookiecutter_json(tmp_path):
    # Create a temporary directory
    repo_directory = tmp_path / "repo"
    repo_directory.mkdir()

    # Test when the directory exists but cookiecutter.json does not
    assert not repository_has_cookiecutter_json(str(repo_directory))

    # Create a cookiecutter.json file in the directory
    cookiecutter_json_path = repo_directory / "cookiecutter.json"
    cookiecutter_json_path.write_text("{}")

    # Test when both the directory and cookiecutter.json exist
    assert repository_has_cookiecutter_json(str(repo_directory))

    # Clean up
    cookiecutter_json_path.unlink()
    repo_directory.rmdir()
