# file cookiecutter/find.py:10-31
# lines [10, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31]
# branches ['21->22', '21->26', '22->21', '22->23', '26->27', '26->31']

import os
import pytest
from cookiecutter.exceptions import NonTemplatedInputDirException
from cookiecutter.find import find_template
from unittest.mock import patch

def test_find_template_with_cookiecutter_dir(tmp_path, mocker):
    # Setup a fake repo directory with a valid template directory
    repo_dir = tmp_path / "fake_repo"
    repo_dir.mkdir()
    template_dir = repo_dir / "cookiecutter-{{fake_project}}"
    template_dir.mkdir()
    
    # Mock the logger to avoid side effects
    mock_logger = mocker.patch('cookiecutter.find.logger')

    # Call the function under test
    found_template = find_template(str(repo_dir))

    # Assertions to check the postconditions
    assert found_template == str(template_dir)
    mock_logger.debug.assert_called_with('The project template appears to be %s', str(template_dir))

def test_find_template_without_cookiecutter_dir(tmp_path, mocker):
    # Setup a fake repo directory without a valid template directory
    repo_dir = tmp_path / "fake_repo"
    repo_dir.mkdir()
    (repo_dir / "not_a_template").mkdir()
    
    # Mock the logger to avoid side effects
    mocker.patch('cookiecutter.find.logger')

    # Call the function under test and assert it raises the correct exception
    with pytest.raises(NonTemplatedInputDirException):
        find_template(str(repo_dir))
