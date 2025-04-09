# file httpie/client.py:176-178
# lines [177, 178]
# branches []

import pytest
import sys
from unittest.mock import patch
from httpie.client import dump_request

def test_dump_request(mocker):
    mock_stderr = mocker.patch('sys.stderr.write')
    kwargs = {'method': 'GET', 'url': 'http://example.com'}

    dump_request(kwargs)

    mock_stderr.assert_called_once_with(
        "\n>>> requests.request(**{'method': 'GET', 'url': 'http://example.com'})\n\n"
    )
