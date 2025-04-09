# file: httpie/config.py:99-121
# asked: {"lines": [99, 100, 101, 103, 104, 106, 107, 109, 111, 112, 113, 114, 115, 117, 118, 119, 120, 121], "branches": [[103, 104], [103, 106], [106, 107], [106, 109], [120, 0], [120, 121]]}
# gained: {"lines": [99, 100, 101, 103, 104, 106, 107, 109, 111, 112, 113, 114, 115, 117, 118, 119, 120, 121], "branches": [[103, 104], [103, 106], [106, 107], [106, 109], [120, 0], [120, 121]]}

import pytest
import json
import errno
from pathlib import Path
from unittest.mock import MagicMock, patch, mock_open
from httpie import __version__
from httpie.config import BaseConfigDict

@pytest.fixture
def config_file(tmp_path):
    return tmp_path / "config.json"

@pytest.fixture
def base_config_dict(config_file):
    return BaseConfigDict(path=config_file)

def test_save_creates_meta_section(base_config_dict, mocker):
    mocker.patch.object(base_config_dict, 'ensure_directory')
    base_config_dict.helpurl = "http://example.com/help"
    base_config_dict.about = "About info"
    
    base_config_dict.save()
    
    assert base_config_dict['__meta__']['httpie'] == __version__
    assert base_config_dict['__meta__']['help'] == "http://example.com/help"
    assert base_config_dict['__meta__']['about'] == "About info"

def test_save_ensures_directory(base_config_dict, mocker):
    ensure_directory_mock = mocker.patch.object(base_config_dict, 'ensure_directory')
    
    base_config_dict.save()
    
    ensure_directory_mock.assert_called_once()

def test_save_writes_json_to_file(base_config_dict, mocker):
    mocker.patch.object(base_config_dict, 'ensure_directory')
    mock_open_obj = mock_open()
    with patch("pathlib.Path.write_text", mock_open_obj):
        base_config_dict.save()
    
    mock_open_obj.assert_called_once()
    written_data = json.loads(mock_open_obj.call_args[0][0])
    assert written_data['__meta__']['httpie'] == __version__

def test_save_handles_ioerror_silently(base_config_dict, mocker):
    mocker.patch.object(base_config_dict, 'ensure_directory')
    mocker.patch("pathlib.Path.write_text", side_effect=IOError)
    
    base_config_dict.save(fail_silently=True)

def test_save_raises_ioerror(base_config_dict, mocker):
    mocker.patch.object(base_config_dict, 'ensure_directory')
    mocker.patch("pathlib.Path.write_text", side_effect=IOError)
    
    with pytest.raises(IOError):
        base_config_dict.save(fail_silently=False)

def test_ensure_directory_creates_directory(base_config_dict, mocker):
    mkdir_mock = mocker.patch("pathlib.Path.mkdir")
    
    base_config_dict.ensure_directory()
    
    mkdir_mock.assert_called_once_with(mode=448, parents=True)

def test_ensure_directory_handles_existing_directory(base_config_dict, mocker):
    error = OSError()
    error.errno = errno.EEXIST
    mkdir_mock = mocker.patch("pathlib.Path.mkdir", side_effect=error)
    
    base_config_dict.ensure_directory()
    
    mkdir_mock.assert_called_once_with(mode=448, parents=True)

def test_ensure_directory_raises_other_oserror(base_config_dict, mocker):
    error = OSError()
    error.errno = errno.EACCES
    mkdir_mock = mocker.patch("pathlib.Path.mkdir", side_effect=error)
    
    with pytest.raises(OSError):
        base_config_dict.ensure_directory()
