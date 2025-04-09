# file cookiecutter/zipfile.py:13-112
# lines [27, 28, 30, 33, 34, 36, 37, 39, 41, 43, 44, 45, 46, 47, 50, 54, 55, 57, 58, 62, 63, 64, 65, 66, 70, 71, 72, 75, 76, 77, 80, 81, 82, 83, 84, 85, 87, 88, 89, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 103, 104, 107, 108, 109, 112]
# branches ['30->33', '30->50', '36->37', '36->39', '41->43', '41->54', '45->46', '45->54', '46->45', '46->47', '57->58', '57->62', '63->64', '63->70', '80->81', '80->87', '87->88', '87->92', '93->94', '93->112', '102->93', '102->103']

import os
import tempfile
import pytest
import requests
from zipfile import ZipFile, BadZipFile
from unittest import mock
from cookiecutter.zipfile import unzip, InvalidZipRepository

@pytest.fixture
def mock_make_sure_path_exists(mocker):
    return mocker.patch('cookiecutter.zipfile.make_sure_path_exists')

@pytest.fixture
def mock_prompt_and_delete(mocker):
    return mocker.patch('cookiecutter.zipfile.prompt_and_delete', return_value=True)

@pytest.fixture
def mock_requests_get(mocker):
    mock_response = mock.Mock()
    mock_response.iter_content = mock.Mock(return_value=[b'content'])
    return mocker.patch('requests.get', return_value=mock_response)

@pytest.fixture
def mock_read_repo_password(mocker):
    return mocker.patch('cookiecutter.zipfile.read_repo_password', return_value='password')

@pytest.fixture
def temp_zip_file():
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, 'test.zip')
    with ZipFile(zip_path, 'w') as zip_file:
        zip_file.writestr('test_dir/', '')
        zip_file.writestr('test_dir/file.txt', 'content')
    yield zip_path
    os.remove(zip_path)
    os.rmdir(temp_dir)

def test_unzip_local_file(mock_make_sure_path_exists, temp_zip_file):
    unzip_path = unzip(temp_zip_file, is_url=False)
    assert os.path.exists(unzip_path)
    assert os.path.isdir(unzip_path)
    assert os.path.exists(os.path.join(unzip_path, 'file.txt'))
    os.remove(os.path.join(unzip_path, 'file.txt'))
    os.rmdir(unzip_path)

def test_unzip_url_file(mock_make_sure_path_exists, mock_prompt_and_delete, mock_requests_get, temp_zip_file):
    with mock.patch('cookiecutter.zipfile.ZipFile', return_value=ZipFile(temp_zip_file)):
        unzip_path = unzip('http://example.com/test.zip', is_url=True)
        assert os.path.exists(unzip_path)
        assert os.path.isdir(unzip_path)
        assert os.path.exists(os.path.join(unzip_path, 'file.txt'))
        os.remove(os.path.join(unzip_path, 'file.txt'))
        os.rmdir(unzip_path)

def test_unzip_password_protected(mock_make_sure_path_exists, mock_read_repo_password, temp_zip_file):
    with ZipFile(temp_zip_file, 'w') as zip_file:
        zip_file.setpassword(b'password')
        zip_file.writestr('test_dir/', '')
        zip_file.writestr('test_dir/file.txt', 'content')
    
    with mock.patch('cookiecutter.zipfile.ZipFile', return_value=ZipFile(temp_zip_file)):
        unzip_path = unzip(temp_zip_file, is_url=False, password='password')
        assert os.path.exists(unzip_path)
        assert os.path.isdir(unzip_path)
        assert os.path.exists(os.path.join(unzip_path, 'file.txt'))
        os.remove(os.path.join(unzip_path, 'file.txt'))
        os.rmdir(unzip_path)

def test_unzip_invalid_zip(mock_make_sure_path_exists):
    with tempfile.TemporaryDirectory() as temp_dir:
        invalid_zip_path = os.path.join(temp_dir, 'invalid.zip')
        with open(invalid_zip_path, 'w') as f:
            f.write('This is not a valid zip file')
        
        with pytest.raises(InvalidZipRepository):
            unzip(invalid_zip_path, is_url=False)
