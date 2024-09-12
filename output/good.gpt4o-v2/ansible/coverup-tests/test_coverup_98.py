# file: lib/ansible/module_utils/urls.py:1835-1872
# asked: {"lines": [1835, 1836, 1837, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872], "branches": [[1863, 1864], [1863, 1865], [1866, 1867], [1866, 1869]]}
# gained: {"lines": [1835, 1836, 1837, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872], "branches": [[1863, 1864], [1863, 1865], [1866, 1867], [1866, 1869]]}

import pytest
import tempfile
from unittest.mock import Mock, patch
from ansible.module_utils.urls import fetch_file

@pytest.fixture
def mock_module():
    module = Mock()
    module.tmpdir = tempfile.gettempdir()
    module.add_cleanup_file = Mock()
    module.fail_json = Mock(side_effect=Exception("Module failed"))
    return module

@patch('ansible.module_utils.urls.fetch_url')
def test_fetch_file_success(mock_fetch_url, mock_module):
    url = "http://example.com/testfile.txt"
    response_mock = Mock()
    response_mock.read = Mock(side_effect=[b"data", b""])
    mock_fetch_url.return_value = (response_mock, {'status': 200})

    result = fetch_file(mock_module, url)

    assert mock_module.add_cleanup_file.called
    assert result.startswith(tempfile.gettempdir())
    with open(result, 'rb') as f:
        assert f.read() == b"data"

@patch('ansible.module_utils.urls.fetch_url')
def test_fetch_file_failure(mock_fetch_url, mock_module):
    url = "http://example.com/testfile.txt"
    mock_fetch_url.return_value = (None, {'msg': 'Not Found'})

    with pytest.raises(Exception, match="Module failed"):
        fetch_file(mock_module, url)

    assert mock_module.fail_json.called

@patch('ansible.module_utils.urls.fetch_url')
def test_fetch_file_exception(mock_fetch_url, mock_module):
    url = "http://example.com/testfile.txt"
    mock_fetch_url.side_effect = Exception("Unexpected error")

    with pytest.raises(Exception, match="Module failed"):
        fetch_file(mock_module, url)

    assert mock_module.fail_json.called
