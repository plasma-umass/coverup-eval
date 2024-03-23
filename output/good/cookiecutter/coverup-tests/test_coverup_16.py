# file cookiecutter/repository.py:63-130
# lines [93, 95, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 118, 119, 120, 123, 124, 125, 127, 128, 129]
# branches ['95->96', '95->105', '105->106', '105->115', '118->119', '118->123', '123->124', '123->127', '124->123', '124->125']

import os
import pytest
from cookiecutter.exceptions import RepositoryNotFound
from cookiecutter.repository import determine_repo_dir
from unittest.mock import patch, mock_open

@pytest.fixture
def cleanup_temp_dir(tmp_path):
    yield tmp_path
    # Cleanup after test
    for item in tmp_path.iterdir():
        if item.is_dir():
            item.rmdir()
        else:
            item.unlink()

def test_determine_repo_dir_with_local_path_and_cookiecutter_json(cleanup_temp_dir, mocker):
    template = str(cleanup_temp_dir)
    abbreviations = {}
    clone_to_dir = str(cleanup_temp_dir)
    checkout = None
    no_input = True
    password = None
    directory = None

    # Mock the functions to simulate the presence of a cookiecutter.json
    mocker.patch('cookiecutter.repository.is_zip_file', return_value=False)
    mocker.patch('cookiecutter.repository.is_repo_url', return_value=False)
    mocker.patch('cookiecutter.repository.repository_has_cookiecutter_json', return_value=True)

    # Create a fake cookiecutter.json file in the temporary directory
    cookiecutter_json_path = os.path.join(template, 'cookiecutter.json')
    with open(cookiecutter_json_path, 'w') as f:
        f.write('{}')

    repo_dir, cleanup = determine_repo_dir(
        template,
        abbreviations,
        clone_to_dir,
        checkout,
        no_input,
        password,
        directory
    )

    assert repo_dir == template
    assert cleanup is False
    assert os.path.isfile(cookiecutter_json_path)

def test_determine_repo_dir_with_local_path_without_cookiecutter_json(cleanup_temp_dir, mocker):
    template = str(cleanup_temp_dir)
    abbreviations = {}
    clone_to_dir = str(cleanup_temp_dir)
    checkout = None
    no_input = True
    password = None
    directory = None

    # Mock the functions to simulate the absence of a cookiecutter.json
    mocker.patch('cookiecutter.repository.is_zip_file', return_value=False)
    mocker.patch('cookiecutter.repository.is_repo_url', return_value=False)
    mocker.patch('cookiecutter.repository.repository_has_cookiecutter_json', return_value=False)

    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(
            template,
            abbreviations,
            clone_to_dir,
            checkout,
            no_input,
            password,
            directory
        )
