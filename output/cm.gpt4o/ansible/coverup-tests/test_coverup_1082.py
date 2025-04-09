# file lib/ansible/module_utils/urls.py:1835-1872
# lines [1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872]
# branches ['1863->1864', '1863->1865', '1866->1867', '1866->1869']

import pytest
import tempfile
import os
from unittest import mock
from ansible.module_utils.urls import fetch_file

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.tmpdir = tempfile.gettempdir()
    module.add_cleanup_file = mocker.Mock()
    module.fail_json = mocker.Mock(side_effect=Exception("fail_json called"))
    return module

@pytest.fixture
def mock_fetch_url(mocker):
    return mocker.patch('ansible.module_utils.urls.fetch_url')

def test_fetch_file_success(mock_module, mock_fetch_url):
    url = "http://example.com/testfile.txt"
    response_mock = mock.Mock()
    response_mock.read = mock.Mock(side_effect=[b"data_chunk_1", b"data_chunk_2", b""])
    mock_fetch_url.return_value = (response_mock, {'status': 200})

    file_path = fetch_file(mock_module, url)

    assert os.path.exists(file_path)
    with open(file_path, 'rb') as f:
        content = f.read()
    assert content == b"data_chunk_1data_chunk_2"

    os.remove(file_path)

def test_fetch_file_failure(mock_module, mock_fetch_url):
    url = "http://example.com/testfile.txt"
    mock_fetch_url.return_value = (None, {'msg': 'Not Found'})

    with pytest.raises(Exception, match="fail_json called"):
        fetch_file(mock_module, url)

def test_fetch_file_exception(mock_module, mock_fetch_url):
    url = "http://example.com/testfile.txt"
    mock_fetch_url.side_effect = Exception("Connection error")

    with pytest.raises(Exception, match="fail_json called"):
        fetch_file(mock_module, url)
