# file cookiecutter/repository.py:63-130
# lines [63, 69, 70, 93, 95, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 118, 119, 120, 123, 124, 125, 127, 128, 129]
# branches ['95->96', '95->105', '105->106', '105->115', '118->119', '118->123', '123->124', '123->127', '124->123', '124->125']

import os
import pytest
from unittest import mock
from cookiecutter.exceptions import RepositoryNotFound
from cookiecutter.repository import determine_repo_dir

@pytest.fixture
def mock_expand_abbreviations(mocker):
    return mocker.patch('cookiecutter.repository.expand_abbreviations', side_effect=lambda x, y: x)

@pytest.fixture
def mock_is_zip_file(mocker):
    return mocker.patch('cookiecutter.repository.is_zip_file', return_value=False)

@pytest.fixture
def mock_is_repo_url(mocker):
    return mocker.patch('cookiecutter.repository.is_repo_url', return_value=False)

@pytest.fixture
def mock_unzip(mocker):
    return mocker.patch('cookiecutter.repository.unzip')

@pytest.fixture
def mock_clone(mocker):
    return mocker.patch('cookiecutter.repository.clone')

@pytest.fixture
def mock_repository_has_cookiecutter_json(mocker):
    return mocker.patch('cookiecutter.repository.repository_has_cookiecutter_json', return_value=False)

def test_determine_repo_dir_local_path(mock_expand_abbreviations, mock_is_zip_file, mock_is_repo_url, mock_unzip, mock_clone, mock_repository_has_cookiecutter_json):
    template = 'local_template'
    abbreviations = {}
    clone_to_dir = 'clone_dir'
    checkout = None
    no_input = True
    password = None
    directory = None

    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)

    mock_expand_abbreviations.assert_called_once_with(template, abbreviations)
    mock_is_zip_file.assert_called_once_with(template)
    mock_is_repo_url.assert_called_once_with(template)
    mock_repository_has_cookiecutter_json.assert_any_call(template)
    mock_repository_has_cookiecutter_json.assert_any_call(os.path.join(clone_to_dir, template))

def test_determine_repo_dir_with_directory(mock_expand_abbreviations, mock_is_zip_file, mock_is_repo_url, mock_unzip, mock_clone, mock_repository_has_cookiecutter_json):
    template = 'local_template'
    abbreviations = {}
    clone_to_dir = 'clone_dir'
    checkout = None
    no_input = True
    password = None
    directory = 'subdir'

    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password, directory)

    mock_expand_abbreviations.assert_called_once_with(template, abbreviations)
    mock_is_zip_file.assert_called_once_with(template)
    mock_is_repo_url.assert_called_once_with(template)
    mock_repository_has_cookiecutter_json.assert_any_call(os.path.join(template, directory))
    mock_repository_has_cookiecutter_json.assert_any_call(os.path.join(clone_to_dir, template, directory))
