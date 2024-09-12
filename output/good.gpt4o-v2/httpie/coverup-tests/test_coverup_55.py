# file: httpie/output/streams.py:129-137
# asked: {"lines": [129, 134, 135, 136, 137], "branches": []}
# gained: {"lines": [129, 134, 135, 136, 137], "branches": []}

import pytest
from httpie.output.streams import PrettyStream
from httpie.output.processing import Conversion, Formatting
from httpie.context import Environment
from unittest.mock import Mock

@pytest.fixture
def mock_msg():
    return Mock(content_type='text/html; charset=UTF-8')

@pytest.fixture
def mock_env():
    env = Mock(spec=Environment)
    env.stdout_isatty = True
    env.stdout_encoding = 'utf-8'
    return env

def test_pretty_stream_initialization(mock_msg, mock_env):
    conversion = Conversion()
    formatting = Formatting(groups=[], env=mock_env)
    stream = PrettyStream(conversion=conversion, formatting=formatting, msg=mock_msg, env=mock_env)
    
    assert stream.formatting == formatting
    assert stream.conversion == conversion
    assert stream.mime == 'text/html'
