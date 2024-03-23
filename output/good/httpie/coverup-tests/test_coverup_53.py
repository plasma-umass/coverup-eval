# file httpie/client.py:176-178
# lines [176, 177, 178]
# branches []

import pytest
from unittest.mock import patch
from httpie.client import dump_request

@pytest.fixture
def mock_stderr():
    with patch('sys.stderr.write') as mock:
        yield mock

def test_dump_request(mock_stderr):
    kwargs = {'method': 'GET', 'url': 'https://example.com'}
    expected_output = "\n>>> requests.request(**{'method': 'GET', 'url': 'https://example.com'})\n\n"

    dump_request(kwargs)

    mock_stderr.assert_called_once_with(expected_output)
