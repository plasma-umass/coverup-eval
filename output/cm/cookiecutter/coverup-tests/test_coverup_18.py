# file cookiecutter/repository.py:63-130
# lines [96, 97, 98, 99, 100, 101, 103, 104, 106, 107, 108, 109, 110, 112, 113, 119, 120]
# branches ['95->96', '105->106', '118->119']

import os
import pytest
from cookiecutter.exceptions import RepositoryNotFound
from cookiecutter.repository import determine_repo_dir
from unittest.mock import patch, MagicMock

@pytest.fixture
def cleanup_temp_dir():
    temp_dirs = []

    yield temp_dirs

    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)

def test_determine_repo_dir_zip_and_repo_url(mocker, cleanup_temp_dir):
    # Mock the functions to simulate different scenarios
    mocker.patch('cookiecutter.repository.is_zip_file', return_value=True)
    mocker.patch('cookiecutter.repository.is_repo_url', return_value=False)
    mocker.patch('cookiecutter.repository.unzip', return_value='fake_unzipped_dir')
    mocker.patch('cookiecutter.repository.repository_has_cookiecutter_json', return_value=True)

    # Add the temporary directory to the cleanup list
    cleanup_temp_dir.append('fake_unzipped_dir')

    # Call the function with the mocked objects
    repo_dir, cleanup = determine_repo_dir(
        template='fake_template',
        abbreviations={},
        clone_to_dir='fake_clone_to_dir',
        checkout='fake_checkout',
        no_input=True,
        password='fake_password',
        directory='fake_directory'
    )

    # Assert the postconditions
    assert repo_dir == os.path.join('fake_unzipped_dir', 'fake_directory')
    assert cleanup is True

    # Now test the branch where the template is a repo URL
    mocker.patch('cookiecutter.repository.is_zip_file', return_value=False)
    mocker.patch('cookiecutter.repository.is_repo_url', return_value=True)
    mocker.patch('cookiecutter.repository.clone', return_value='fake_cloned_repo')

    # Call the function with the mocked objects
    repo_dir, cleanup = determine_repo_dir(
        template='fake_template',
        abbreviations={},
        clone_to_dir='fake_clone_to_dir',
        checkout='fake_checkout',
        no_input=True,
        password=None,
        directory=None
    )

    # Assert the postconditions
    assert repo_dir == 'fake_cloned_repo'
    assert cleanup is False

    # Test the branch where the directory is specified
    mocker.patch('cookiecutter.repository.is_zip_file', return_value=False)
    mocker.patch('cookiecutter.repository.is_repo_url', return_value=False)

    # Call the function with the mocked objects
    repo_dir, cleanup = determine_repo_dir(
        template='fake_template',
        abbreviations={},
        clone_to_dir='fake_clone_to_dir',
        checkout=None,
        no_input=False,
        password=None,
        directory='fake_directory'
    )

    # Assert the postconditions
    assert repo_dir.endswith('fake_directory')
    assert cleanup is False

    # Test the branch where the repository is not found
    mocker.patch('cookiecutter.repository.repository_has_cookiecutter_json', return_value=False)

    with pytest.raises(RepositoryNotFound):
        determine_repo_dir(
            template='fake_template',
            abbreviations={},
            clone_to_dir='fake_clone_to_dir',
            checkout=None,
            no_input=False,
            password=None,
            directory='fake_directory'
        )
