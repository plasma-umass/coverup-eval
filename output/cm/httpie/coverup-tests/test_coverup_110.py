# file httpie/output/streams.py:129-137
# lines [134, 135, 136, 137]
# branches []

import pytest
from httpie.output.streams import PrettyStream
from httpie.plugins import FormatterPlugin
from httpie.output.formatters.colors import Solarized256Style
from httpie.output.formatters.colors import ColorFormatter
from requests.structures import CaseInsensitiveDict

class DummyFormatter(FormatterPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def format_headers(self, headers):
        return headers

    def format_body(self, body, mime):
        return body

@pytest.fixture
def mock_conversion(mocker):
    return mocker.Mock()

@pytest.fixture
def mock_formatting(mocker):
    return mocker.Mock()

@pytest.fixture
def mock_msg(mocker):
    msg = mocker.Mock()
    msg.content_type = 'text/plain;charset=utf-8'
    return msg

def test_pretty_stream_initialization(mock_conversion, mock_formatting, mock_msg):
    stream = PrettyStream(
        conversion=mock_conversion,
        formatting=mock_formatting,
        msg=mock_msg
    )
    assert stream.formatting == mock_formatting
    assert stream.conversion == mock_conversion
    assert stream.mime == 'text/plain'
