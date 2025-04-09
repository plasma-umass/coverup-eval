# file httpie/output/writer.py:19-51
# lines [27]
# branches ['26->27']

import pytest
import argparse
from unittest.mock import Mock
from httpie.output.writer import write_message
from httpie.context import Environment
import requests

def test_write_message_no_headers_no_body(mocker):
    # Mock the requests message
    requests_message = Mock(spec=requests.PreparedRequest)
    
    # Mock the environment
    env = Mock(spec=Environment)
    env.stdout = Mock()
    env.stdout_isatty = False
    env.is_windows = False
    env.stderr = Mock()
    
    # Create argparse.Namespace with necessary attributes
    args = argparse.Namespace()
    args.stream = False
    args.prettify = []
    args.debug = False
    args.traceback = False
    
    # Call the function with with_headers and with_body as False
    write_message(requests_message, env, args, with_headers=False, with_body=False)
    
    # Assert that the function returned early and did not write to stdout
    env.stdout.write.assert_not_called()
    env.stderr.write.assert_not_called()
