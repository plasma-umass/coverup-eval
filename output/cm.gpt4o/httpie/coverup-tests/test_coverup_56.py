# file httpie/output/streams.py:129-137
# lines [129, 134, 135, 136, 137]
# branches []

import pytest
from unittest.mock import Mock
from httpie.output.streams import PrettyStream, Conversion, Formatting

def test_pretty_stream_initialization():
    mock_msg = Mock()
    mock_msg.content_type = 'text/html; charset=UTF-8'
    
    conversion = Conversion()
    formatting = Formatting(groups=[])
    
    stream = PrettyStream(conversion=conversion, formatting=formatting, msg=mock_msg)
    
    assert stream.formatting == formatting
    assert stream.conversion == conversion
    assert stream.mime == 'text/html'
