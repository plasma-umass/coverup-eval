# file thefuck/rules/dirty_unzip.py:28-37
# lines [28, 29, 30, 31, 33, 34, 35, 37]
# branches ['30->31', '30->33', '34->35', '34->37']

import pytest
from thefuck.rules.dirty_unzip import match
from thefuck.types import Command

@pytest.fixture
def mock_zip_file(mocker):
    return mocker.patch('thefuck.rules.dirty_unzip._zip_file')

@pytest.fixture
def mock_is_bad_zip(mocker):
    return mocker.patch('thefuck.rules.dirty_unzip._is_bad_zip')

def test_match_with_dash_d_in_script():
    command = Command(script='unzip -d somefile.zip', output='')
    assert not match(command)

def test_match_with_no_zip_file(mock_zip_file):
    mock_zip_file.return_value = None
    command = Command(script='unzip somefile.zip', output='')
    assert not match(command)

def test_match_with_bad_zip_file(mock_zip_file, mock_is_bad_zip):
    mock_zip_file.return_value = 'somefile.zip'
    mock_is_bad_zip.return_value = True
    command = Command(script='unzip somefile.zip', output='')
    assert match(command)

def test_match_with_good_zip_file(mock_zip_file, mock_is_bad_zip):
    mock_zip_file.return_value = 'somefile.zip'
    mock_is_bad_zip.return_value = False
    command = Command(script='unzip somefile.zip', output='')
    assert not match(command)
