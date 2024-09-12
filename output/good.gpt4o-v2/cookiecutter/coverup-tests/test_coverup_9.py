# file: cookiecutter/repository.py:49-60
# asked: {"lines": [49, 55, 57, 58, 60], "branches": []}
# gained: {"lines": [49, 55, 57, 58, 60], "branches": []}

import os
import pytest
from unittest import mock
from cookiecutter.repository import repository_has_cookiecutter_json

def test_repository_has_cookiecutter_json_with_valid_directory_and_file():
    with mock.patch('os.path.isdir') as mock_isdir, \
         mock.patch('os.path.isfile') as mock_isfile:
        mock_isdir.return_value = True
        mock_isfile.return_value = True

        result = repository_has_cookiecutter_json('some/repo/directory')
        assert result is True

def test_repository_has_cookiecutter_json_with_valid_directory_but_no_file():
    with mock.patch('os.path.isdir') as mock_isdir, \
         mock.patch('os.path.isfile') as mock_isfile:
        mock_isdir.return_value = True
        mock_isfile.return_value = False

        result = repository_has_cookiecutter_json('some/repo/directory')
        assert result is False

def test_repository_has_cookiecutter_json_with_invalid_directory():
    with mock.patch('os.path.isdir') as mock_isdir, \
         mock.patch('os.path.isfile') as mock_isfile:
        mock_isdir.return_value = False
        mock_isfile.return_value = False

        result = repository_has_cookiecutter_json('some/repo/directory')
        assert result is False

def test_repository_has_cookiecutter_json_with_invalid_directory_but_file_exists():
    with mock.patch('os.path.isdir') as mock_isdir, \
         mock.patch('os.path.isfile') as mock_isfile:
        mock_isdir.return_value = False
        mock_isfile.return_value = True

        result = repository_has_cookiecutter_json('some/repo/directory')
        assert result is False
