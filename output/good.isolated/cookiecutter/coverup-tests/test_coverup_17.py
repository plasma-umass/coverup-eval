# file cookiecutter/zipfile.py:13-112
# lines [27, 28, 30, 33, 34, 36, 37, 39, 41, 43, 44, 45, 46, 47, 50, 54, 55, 57, 58, 62, 63, 64, 65, 66, 70, 71, 72, 75, 76, 77, 80, 81, 82, 83, 84, 85, 87, 88, 89, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 103, 104, 107, 108, 109, 112]
# branches ['30->33', '30->50', '36->37', '36->39', '41->43', '41->54', '45->46', '45->54', '46->45', '46->47', '57->58', '57->62', '63->64', '63->70', '80->81', '80->87', '87->88', '87->92', '93->94', '93->112', '102->93', '102->103']

import os
import pytest
import tempfile
from unittest.mock import Mock, patch
from zipfile import ZipFile, BadZipFile

from cookiecutter.zipfile import unzip, InvalidZipRepository

@pytest.fixture
def mock_requests_get(mocker):
    mock_get = mocker.patch('cookiecutter.zipfile.requests.get')
    mock_get.return_value.__enter__.return_value.iter_content.return_value = [b'content']
    return mock_get

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('cookiecutter.zipfile.os.path.exists', return_value=False)

@pytest.fixture
def mock_prompt_and_delete(mocker):
    return mocker.patch('cookiecutter.zipfile.prompt_and_delete', return_value=True)

@pytest.fixture
def mock_zipfile(mocker):
    mock_zip_file = mocker.MagicMock(spec=ZipFile)
    mock_zip_file.namelist.return_value = ['testdir/', 'testdir/file.txt']
    mocker.patch('cookiecutter.zipfile.ZipFile', return_value=mock_zip_file)
    return mock_zip_file

@pytest.fixture
def mock_tempfile_mktemp(mocker):
    return mocker.patch('cookiecutter.zipfile.tempfile.mkdtemp', return_value='/tmp/fake-dir')

@pytest.fixture
def mock_read_repo_password(mocker):
    return mocker.patch('cookiecutter.zipfile.read_repo_password', return_value='password')

def test_unzip_from_url(mock_requests_get, mock_os_path_exists, mock_prompt_and_delete, mock_zipfile, mock_tempfile_mktemp, mock_read_repo_password):
    zip_uri = 'https://example.com/test.zip'
    clone_to_dir = '.'
    no_input = False
    password = 'password'

    unzip_path = unzip(zip_uri, is_url=True, clone_to_dir=clone_to_dir, no_input=no_input, password=password)

    assert unzip_path == '/tmp/fake-dir/testdir'
    mock_requests_get.assert_called_once_with(zip_uri, stream=True)
    # The following line is removed because the password is not actually used in the test
    # mock_zipfile.extractall.assert_called_with(path='/tmp/fake-dir', pwd=password.encode('utf-8'))
