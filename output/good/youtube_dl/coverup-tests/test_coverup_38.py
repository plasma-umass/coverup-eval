# file youtube_dl/downloader/common.py:248-306
# lines [249, 250, 251, 253, 254, 255, 256, 257, 258, 259, 260, 261, 263, 264, 266, 267, 269, 270, 272, 274, 275, 276, 277, 279, 280, 282, 284, 285, 287, 289, 290, 291, 292, 293, 294, 296, 297, 298, 299, 300, 302, 304, 306]
# branches ['249->250', '249->263', '250->251', '250->253', '254->255', '254->257', '257->258', '257->260', '263->264', '263->266', '266->267', '266->269', '269->270', '269->272', '274->275', '274->276', '276->277', '276->279', '279->280', '279->282', '284->285', '284->287', '289->290', '289->292', '292->293', '292->296', '296->297', '296->304', '298->299', '298->302']

import pytest
from youtube_dl.downloader.common import FileDownloader

@pytest.fixture
def mock_file_downloader(mocker):
    mocker.patch('youtube_dl.downloader.common.FileDownloader._report_progress_status')
    mocker.patch('youtube_dl.downloader.common.FileDownloader.to_screen')
    mocker.patch('youtube_dl.downloader.common.FileDownloader.format_seconds')
    mocker.patch('youtube_dl.downloader.common.FileDownloader.format_eta')
    mocker.patch('youtube_dl.downloader.common.FileDownloader.format_percent')
    mocker.patch('youtube_dl.downloader.common.FileDownloader.format_speed')
    mocker.patch('youtube_dl.downloader.common.format_bytes', return_value='1.00KiB')
    fd = FileDownloader(None, {})
    return fd

def test_report_progress_finished(mock_file_downloader):
    status = {
        'status': 'finished',
        'total_bytes': 1024,
        'elapsed': 1.0
    }
    mock_file_downloader.report_progress(status)
    mock_file_downloader._report_progress_status.assert_called_once()
    mock_file_downloader.to_screen.assert_not_called()

def test_report_progress_finished_noprogress(mock_file_downloader):
    mock_file_downloader.params['noprogress'] = True
    status = {'status': 'finished'}
    mock_file_downloader.report_progress(status)
    mock_file_downloader.to_screen.assert_called_once_with('[download] Download completed')
    mock_file_downloader._report_progress_status.assert_not_called()

def test_report_progress_downloading(mock_file_downloader):
    status = {
        'status': 'downloading',
        'eta': 10,
        'total_bytes': 1024,
        'downloaded_bytes': 512,
        'speed': 1024.0
    }
    mock_file_downloader.report_progress(status)
    mock_file_downloader._report_progress_status.assert_called_once()
    mock_file_downloader.format_eta.assert_called_once_with(10)
    mock_file_downloader.format_percent.assert_called_once()
    mock_file_downloader.format_speed.assert_called_once_with(1024.0)

def test_report_progress_downloading_no_eta(mock_file_downloader):
    status = {
        'status': 'downloading',
        'total_bytes': 1024,
        'downloaded_bytes': 512,
        'speed': 1024.0
    }
    mock_file_downloader.report_progress(status)
    mock_file_downloader._report_progress_status.assert_called_once()
    mock_file_downloader.format_eta.assert_not_called()

def test_report_progress_downloading_no_speed(mock_file_downloader):
    status = {
        'status': 'downloading',
        'eta': 10,
        'total_bytes': 1024,
        'downloaded_bytes': 512
    }
    mock_file_downloader.report_progress(status)
    mock_file_downloader._report_progress_status.assert_called_once()
    mock_file_downloader.format_speed.assert_not_called()

def test_report_progress_downloading_estimate(mock_file_downloader):
    status = {
        'status': 'downloading',
        'eta': 10,
        'total_bytes_estimate': 2048,
        'downloaded_bytes': 512,
        'speed': 1024.0
    }
    mock_file_downloader.report_progress(status)
    mock_file_downloader._report_progress_status.assert_called_once()
    mock_file_downloader.format_percent.assert_called_once()

def test_report_progress_downloading_no_total_bytes(mock_file_downloader):
    status = {
        'status': 'downloading',
        'eta': 10,
        'downloaded_bytes': 0,
        'speed': 1024.0
    }
    mock_file_downloader.report_progress(status)
    mock_file_downloader._report_progress_status.assert_called_once()
    mock_file_downloader.format_percent.assert_called_once_with(0)

def test_report_progress_downloading_no_downloaded_bytes(mock_file_downloader):
    status = {
        'status': 'downloading',
        'eta': 10,
        'total_bytes': 1024,
        'speed': 1024.0
    }
    mock_file_downloader.report_progress(status)
    mock_file_downloader._report_progress_status.assert_called_once()
    mock_file_downloader.format_percent.assert_not_called()

def test_report_progress_downloading_no_total_bytes_no_estimate(mock_file_downloader):
    status = {
        'status': 'downloading',
        'eta': 10,
        'downloaded_bytes': 512,
        'speed': 1024.0
    }
    mock_file_downloader.report_progress(status)
    mock_file_downloader._report_progress_status.assert_called_once()
    mock_file_downloader.format_percent.assert_not_called()
