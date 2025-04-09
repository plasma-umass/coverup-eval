# file: httpie/output/streams.py:164-170
# asked: {"lines": [164, 165, 168, 169, 170], "branches": [[165, 168], [165, 169]]}
# gained: {"lines": [164, 165, 168, 169, 170], "branches": [[165, 168], [165, 169]]}

import pytest
from httpie.output.streams import PrettyStream
from httpie.output.processing import Conversion, Formatting
from httpie.context import Environment
from unittest.mock import Mock

@pytest.fixture
def pretty_stream():
    env = Environment()
    env.stdout_isatty = True
    env.stdout_encoding = 'utf-8'
    msg = Mock()
    msg.encoding = 'utf-8'
    msg.content_type = 'text/plain; charset=utf-8'
    conversion = Conversion()
    formatting = Formatting(groups=[])
    return PrettyStream(conversion=conversion, formatting=formatting, env=env, msg=msg)

def test_process_body_with_bytes(pretty_stream):
    chunk = b'test bytes'
    result = pretty_stream.process_body(chunk)
    assert isinstance(result, bytes)
    assert result == b'test bytes'

def test_process_body_with_str(pretty_stream):
    chunk = 'test string'
    result = pretty_stream.process_body(chunk)
    assert isinstance(result, bytes)
    assert result == b'test string'

def test_process_body_with_non_utf8_encoding(pretty_stream, monkeypatch):
    chunk = b'test bytes'
    pretty_stream.msg.encoding = 'latin-1'
    monkeypatch.setattr(pretty_stream, 'output_encoding', 'latin-1')
    result = pretty_stream.process_body(chunk)
    assert isinstance(result, bytes)
    assert result == b'test bytes'.decode('latin-1').encode('latin-1')
