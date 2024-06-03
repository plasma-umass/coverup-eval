# file cookiecutter/repository.py:63-130
# lines [96, 97, 98, 99, 100, 101, 103, 104, 106, 107, 108, 109, 110, 112, 113, 125]
# branches ['95->96', '105->106', '124->125']

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

def test_determine_repo_dir_zip_file(mock_expand_abbreviations, mock_is_zip_file, mock_unzip, mock_repository_has_cookiecutter_json):
    mock_is_zip_file.return_value = True
    mock_unzip.return_value = 'unzipped_dir'
    mock_repository_has_cookiecutter_json.side_effect = lambda x: x == 'unzipped_dir'

    result = determine_repo_dir(
        template='template.zip',
        abbreviations={},
        clone_to_dir='clone_to_dir',
        checkout=None,
        no_input=True,
        password=None,
        directory=None,
    )

    assert result == ('unzipped_dir', True)
    mock_unzip.assert_called_once_with(
        zip_uri='template.zip',
        is_url=False,
        clone_to_dir='clone_to_dir',
        no_input=True,
        password=None,
    )

def test_determine_repo_dir_repo_url(mock_expand_abbreviations, mock_is_zip_file, mock_is_repo_url, mock_clone, mock_repository_has_cookiecutter_json):
    mock_is_repo_url.return_value = True
    mock_clone.return_value = 'cloned_repo'
    mock_repository_has_cookiecutter_json.side_effect = lambda x: x == 'cloned_repo'

    result = determine_repo_dir(
        template='https://github.com/user/repo.git',
        abbreviations={},
        clone_to_dir='clone_to_dir',
        checkout='main',
        no_input=True,
        password=None,
        directory=None,
    )

    assert result == ('cloned_repo', False)
    mock_clone.assert_called_once_with(
        repo_url='https://github.com/user/repo.git',
        checkout='main',
        clone_to_dir='clone_to_dir',
        no_input=True,
    )

def test_determine_repo_dir_local_path(mock_expand_abbreviations, mock_is_zip_file, mock_is_repo_url, mock_repository_has_cookiecutter_json):
    mock_repository_has_cookiecutter_json.side_effect = lambda x: x == 'template'

    result = determine_repo_dir(
        template='template',
        abbreviations={},
        clone_to_dir='clone_to_dir',
        checkout=None,
        no_input=True,
        password=None,
        directory=None,
    )

    assert result == ('template', False)

def test_determine_repo_dir_with_directory(mock_expand_abbreviations, mock_is_zip_file, mock_is_repo_url, mock_repository_has_cookiecutter_json):
    mock_repository_has_cookiecutter_json.side_effect = lambda x: x == os.path.join('template', 'subdir')

    result = determine_repo_dir(
        template='template',
        abbreviations={},
        clone_to_dir='clone_to_dir',
        checkout=None,
        no_input=True,
        password=None,
        directory='subdir',
    )

    assert result == (os.path.join('template', 'subdir'), False)

def test_determine_repo_dir_not_found(mock_expand_abbreviations, mock_is_zip_file, mock_is_repo_url, mock_repository_has_cookiecutter_json):
    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(
            template='template',
            abbreviations={},
            clone_to_dir='clone_to_dir',
            checkout=None,
            no_input=True,
            password=None,
            directory=None,
        )
