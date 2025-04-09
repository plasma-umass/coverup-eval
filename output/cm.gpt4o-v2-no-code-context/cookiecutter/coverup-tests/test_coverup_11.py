# file: cookiecutter/repository.py:63-130
# asked: {"lines": [63, 69, 70, 93, 95, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 118, 119, 120, 123, 124, 125, 127, 128, 129], "branches": [[95, 96], [95, 105], [105, 106], [105, 115], [118, 119], [118, 123], [123, 124], [123, 127], [124, 123], [124, 125]]}
# gained: {"lines": [63, 69, 70, 93, 95, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 118, 119, 120, 123, 124, 125, 127, 128, 129], "branches": [[95, 96], [95, 105], [105, 106], [105, 115], [118, 119], [118, 123], [123, 124], [123, 127], [124, 123], [124, 125]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from cookiecutter.repository import determine_repo_dir, RepositoryNotFound

@pytest.fixture
def mock_expand_abbreviations():
    with patch('cookiecutter.repository.expand_abbreviations') as mock:
        yield mock

@pytest.fixture
def mock_is_zip_file():
    with patch('cookiecutter.repository.is_zip_file') as mock:
        yield mock

@pytest.fixture
def mock_unzip():
    with patch('cookiecutter.repository.unzip') as mock:
        yield mock

@pytest.fixture
def mock_is_repo_url():
    with patch('cookiecutter.repository.is_repo_url') as mock:
        yield mock

@pytest.fixture
def mock_clone():
    with patch('cookiecutter.repository.clone') as mock:
        yield mock

@pytest.fixture
def mock_repository_has_cookiecutter_json():
    with patch('cookiecutter.repository.repository_has_cookiecutter_json') as mock:
        yield mock

def test_determine_repo_dir_zip_file(mock_expand_abbreviations, mock_is_zip_file, mock_unzip, mock_is_repo_url, mock_repository_has_cookiecutter_json):
    mock_expand_abbreviations.return_value = 'template.zip'
    mock_is_zip_file.return_value = True
    mock_unzip.return_value = 'unzipped_dir'
    mock_is_repo_url.return_value = False
    mock_repository_has_cookiecutter_json.return_value = True

    result = determine_repo_dir(
        template='template.zip',
        abbreviations={},
        clone_to_dir='.',
        checkout=None,
        no_input=True
    )

    assert result == ('unzipped_dir', True)

def test_determine_repo_dir_repo_url(mock_expand_abbreviations, mock_is_zip_file, mock_clone, mock_repository_has_cookiecutter_json):
    mock_expand_abbreviations.return_value = 'https://github.com/example/repo.git'
    mock_is_zip_file.return_value = False
    mock_clone.return_value = 'cloned_repo'
    mock_repository_has_cookiecutter_json.return_value = True

    result = determine_repo_dir(
        template='https://github.com/example/repo.git',
        abbreviations={},
        clone_to_dir='.',
        checkout='main',
        no_input=True
    )

    assert result == ('cloned_repo', False)

def test_determine_repo_dir_local_path(mock_expand_abbreviations, mock_is_zip_file, mock_repository_has_cookiecutter_json):
    mock_expand_abbreviations.return_value = 'local_template'
    mock_is_zip_file.return_value = False
    mock_repository_has_cookiecutter_json.side_effect = lambda x: x == 'local_template'

    result = determine_repo_dir(
        template='local_template',
        abbreviations={},
        clone_to_dir='.',
        checkout=None,
        no_input=True
    )

    assert result == ('local_template', False)

def test_determine_repo_dir_with_directory(mock_expand_abbreviations, mock_is_zip_file, mock_repository_has_cookiecutter_json):
    mock_expand_abbreviations.return_value = 'local_template'
    mock_is_zip_file.return_value = False
    mock_repository_has_cookiecutter_json.side_effect = lambda x: x == 'local_template/subdir'

    result = determine_repo_dir(
        template='local_template',
        abbreviations={},
        clone_to_dir='.',
        checkout=None,
        no_input=True,
        directory='subdir'
    )

    assert result == ('local_template/subdir', False)

def test_determine_repo_dir_not_found(mock_expand_abbreviations, mock_is_zip_file, mock_repository_has_cookiecutter_json):
    mock_expand_abbreviations.return_value = 'non_existent_template'
    mock_is_zip_file.return_value = False
    mock_repository_has_cookiecutter_json.return_value = False

    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(
            template='non_existent_template',
            abbreviations={},
            clone_to_dir='.',
            checkout=None,
            no_input=True
        )
