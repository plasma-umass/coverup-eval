# file youtube_dl/downloader/common.py:91-101
# lines [93, 94, 95, 96, 97, 98, 99, 100, 101]
# branches ['93->94', '93->95', '95->96', '95->97', '98->99', '98->100']

import pytest
from youtube_dl.downloader.common import FileDownloader
import time

def test_calc_eta_none_total(mocker):
    mocker.patch('time.time', return_value=10)
    eta = FileDownloader.calc_eta(start=0, now=None, total=None, current=0)
    assert eta is None

def test_calc_eta_none_current_zero(mocker):
    mocker.patch('time.time', return_value=10)
    eta = FileDownloader.calc_eta(start=0, now=None, total=1000, current=0)
    assert eta is None

def test_calc_eta_none_dif_too_small(mocker):
    mocker.patch('time.time', return_value=0.0005)
    eta = FileDownloader.calc_eta(start=0, now=None, total=1000, current=500)
    assert eta is None

def test_calc_eta_positive(mocker):
    start_time = 0
    now_time = 10
    total_size = 1000
    current_size = 500
    mocker.patch('time.time', return_value=now_time)
    eta = FileDownloader.calc_eta(start=start_time, now=None, total=total_size, current=current_size)
    expected_eta = int((float(total_size) - float(current_size)) / (float(current_size) / (now_time - start_time)))
    assert eta == expected_eta
