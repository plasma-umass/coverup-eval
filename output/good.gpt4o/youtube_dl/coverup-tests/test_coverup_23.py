# file youtube_dl/options.py:23-38
# lines [24, 25, 27, 28, 29, 30, 32, 34, 35, 36, 37, 38]
# branches ['29->30', '29->32', '35->36', '35->38', '36->35', '36->37']

import pytest
import re
from unittest import mock

# Assuming the function _hide_login_info is defined in the module youtube_dl.options
from youtube_dl.options import _hide_login_info

def test_hide_login_info():
    opts = ['--username', 'user123', '--password', 'pass123', '--video-password=vidpass123', '--other-option', 'value']
    expected = ['--username', 'PRIVATE', '--password', 'PRIVATE', '--video-password=PRIVATE', '--other-option', 'value']
    
    result = _hide_login_info(opts)
    
    assert result == expected

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
