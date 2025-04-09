# file cookiecutter/find.py:10-31
# lines [10, 16, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31]
# branches ['21->22', '21->26', '22->21', '22->23', '26->27', '26->31']

import os
import pytest
import logging
from unittest import mock
from cookiecutter.find import find_template, NonTemplatedInputDirException

# Mock logger to avoid actual logging during tests
logger = logging.getLogger('cookiecutter.find')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

def test_find_template_success(tmp_path):
    # Create a temporary directory and a mock template file
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    template_file = repo_dir / "cookiecutter-{{project_name}}"
    template_file.touch()

    # Call the function and assert the correct template path is returned
    result = find_template(str(repo_dir))
    assert result == str(template_file)

def test_find_template_failure(tmp_path):
    # Create a temporary directory without a valid template file
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    invalid_file = repo_dir / "not_a_template"
    invalid_file.touch()

    # Call the function and assert the exception is raised
    with pytest.raises(NonTemplatedInputDirException):
        find_template(str(repo_dir))

# Mock os.listdir to simulate different directory contents
def test_find_template_mocked(mocker):
    repo_dir = "/mocked/repo"
    mocker.patch('os.listdir', return_value=['cookiecutter-{{project_name}}'])

    result = find_template(repo_dir)
    assert result == os.path.join(repo_dir, 'cookiecutter-{{project_name}}')

def test_find_template_no_template_mocked(mocker):
    repo_dir = "/mocked/repo"
    mocker.patch('os.listdir', return_value=['not_a_template'])

    with pytest.raises(NonTemplatedInputDirException):
        find_template(repo_dir)
