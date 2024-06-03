# file httpie/core.py:128-218
# lines [128, 134, 135, 136, 137, 139, 140, 142, 143, 145, 147, 149, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 166, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 195, 196, 197, 199, 200, 201, 203, 204, 205, 206, 207, 208, 209, 210, 212, 215, 216, 217, 218]
# branches ['151->exit', '151->152', '159->160', '159->163', '169->170', '169->195', '173->175', '173->176', '177->178', '177->185', '178->179', '178->190', '181->182', '181->190', '186->187', '186->190', '188->189', '188->190', '195->196', '195->197', '197->199', '197->212', '205->206', '205->212', '215->216', '215->217', '217->exit', '217->218']

import pytest
from unittest.mock import MagicMock, patch
from httpie.core import program, ExitStatus
from httpie.context import Environment
import argparse
import requests

@pytest.fixture
def mock_env():
    env = MagicMock(spec=Environment)
    env.stdout_isatty = True
    env.stdout = MagicMock()
    env.stderr = MagicMock()
    env.config.directory = '/mock/config/dir'
    return env

@pytest.fixture
def mock_args():
    args = MagicMock(spec=argparse.Namespace)
    args.download = True
    args.follow = False
    args.download_resume = False
    args.output_file = MagicMock()
    args.output_file_specified = True
    args.headers = {}
    args.output_options = []
    args.check_status = False
    args.quiet = False
    return args

@patch('httpie.core.collect_messages')
@patch('httpie.core.Downloader')
@patch('httpie.core.write_message')
@patch('httpie.core.get_output_options')
@patch('httpie.core.http_status_to_exit_status')
@patch('httpie.core.write_stream')
def test_program_full_coverage(mock_write_stream, mock_http_status_to_exit_status, mock_get_output_options, mock_write_message, mock_downloader, mock_collect_messages, mock_args, mock_env):
    # Mocking the collect_messages to return a sequence of messages
    mock_request = MagicMock(spec=requests.PreparedRequest)
    mock_request.body = b'test body'
    mock_request.headers = {}
    mock_request.url = 'http://example.com'
    
    mock_response = MagicMock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.raw = MagicMock()
    mock_response.raw.status = '200 OK'
    mock_response.raw.reason = 'OK'
    
    mock_collect_messages.return_value = [mock_request, mock_response]
    mock_get_output_options.return_value = (True, True)
    mock_http_status_to_exit_status.return_value = ExitStatus.SUCCESS
    
    # Mocking the Downloader instance
    mock_downloader_instance = mock_downloader.return_value
    mock_downloader_instance.finished = False
    mock_downloader_instance.interrupted = False
    mock_downloader_instance.status.total_size = 100
    mock_downloader_instance.status.downloaded = 100
    mock_downloader_instance.start.return_value = (b'stream', mock_args.output_file)
    
    exit_status = program(mock_args, mock_env)
    
    assert exit_status == ExitStatus.SUCCESS
    mock_write_message.assert_called()
    mock_write_stream.assert_called()
    mock_downloader_instance.finish.assert_called()
    mock_downloader_instance.pre_request.assert_called_with(mock_args.headers)
    mock_downloader_instance.start.assert_called_with(initial_url=mock_request.url, final_response=mock_response)
    mock_downloader_instance.finish.assert_called()
    
    # Ensure cleanup
    mock_args.output_file.close.assert_called()
    if mock_downloader_instance.finished:
        mock_downloader_instance.failed.assert_not_called()
    else:
        mock_downloader_instance.failed.assert_called()
