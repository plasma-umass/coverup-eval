# file youtube_dl/downloader/common.py:329-366
# lines [334, 335, 336, 339, 340, 341, 342, 343, 347, 348, 349, 350, 351, 352, 354, 356, 357, 358, 359, 360, 361, 362, 363, 364, 366]
# branches ['339->340', '339->356', '347->348', '347->356', '357->358', '357->366']

import os
import pytest
from youtube_dl.downloader.common import FileDownloader
from unittest.mock import MagicMock

class MockYDL:
    params = {}

@pytest.fixture
def mock_file_downloader(mocker):
    # Mock the FileDownloader class
    ydl = MockYDL()
    fd = FileDownloader(ydl, ydl.params)
    mocker.patch.object(fd, 'report_file_already_downloaded')
    mocker.patch.object(fd, '_hook_progress')
    mocker.patch.object(fd, 'to_screen')
    mocker.patch.object(fd, 'real_download', return_value=True)
    return fd

def test_download_nooverwrites_and_exists(mock_file_downloader, tmp_path, mocker):
    # Create a temporary file to simulate an existing file
    filename = tmp_path / "testfile.txt"
    filename.touch()

    # Set the parameters to trigger nooverwrites_and_exists
    mock_file_downloader.params['nooverwrites'] = True

    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('os.path.getsize', return_value=1234)

    # Call the download method
    result = mock_file_downloader.download(str(filename), {})

    # Assert that the file already downloaded message was triggered
    mock_file_downloader.report_file_already_downloaded.assert_called_once_with(str(filename))
    mock_file_downloader._hook_progress.assert_called_once()

    # Assert that the method returned True
    assert result == True

def test_download_continuedl_and_exists(mock_file_downloader, tmp_path, mocker):
    # Create a temporary file to simulate an existing file
    filename = tmp_path / "testfile.txt"
    filename.touch()

    # Set the parameters to trigger continuedl_and_exists
    mock_file_downloader.params['continuedl'] = True
    mock_file_downloader.params['nopart'] = False

    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isfile', return_value=True)
    mocker.patch('os.path.getsize', return_value=1234)

    # Call the download method
    result = mock_file_downloader.download(str(filename), {})

    # Assert that the file already downloaded message was triggered
    mock_file_downloader.report_file_already_downloaded.assert_called_once_with(str(filename))
    mock_file_downloader._hook_progress.assert_called_once()

    # Assert that the method returned True
    assert result == True

def test_download_sleep_interval(mock_file_downloader, mocker):
    # Set the parameters to trigger sleep_interval
    mock_file_downloader.params['sleep_interval'] = 1
    mock_file_downloader.params['max_sleep_interval'] = 2

    # Mock time.sleep to avoid actual sleeping
    mocker.patch('time.sleep', return_value=None)

    # Call the download method
    result = mock_file_downloader.download('testfile', {})

    # Assert that the to_screen method was called with the sleep message
    mock_file_downloader.to_screen.assert_called_once()
    assert 'Sleeping' in mock_file_downloader.to_screen.call_args[0][0]

    # Assert that the method returned True
    assert result == True
