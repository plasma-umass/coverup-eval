# file: httpie/output/writer.py:121-156
# asked: {"lines": [121, 128, 129, 130, 131, 132, 133, 134, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 151, 152, 153, 156], "branches": [[128, 129], [128, 137], [137, 138], [137, 151]]}
# gained: {"lines": [121, 128, 129, 130, 131, 132, 133, 134, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 151, 152, 153, 156], "branches": [[128, 129], [128, 137], [137, 138], [137, 151]]}

import argparse
import pytest
from httpie.context import Environment
from httpie.output.writer import get_stream_type_and_kwargs
from httpie.output.streams import RawStream, PrettyStream, BufferedPrettyStream, EncodedStream
from httpie.output.processing import Formatting
from unittest.mock import patch

@pytest.fixture
def mock_env(mocker):
    env = Environment()
    mocker.patch.object(env, 'stdout_isatty', False)
    return env

@pytest.fixture
def mock_plugin_manager():
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={
        'group1': [],
        'group2': []
    }):
        yield

def test_get_stream_type_and_kwargs_raw_stream(mock_env):
    args = argparse.Namespace(prettify=False, stream=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, args)
    assert stream_class == RawStream
    assert stream_kwargs == {'chunk_size': RawStream.CHUNK_SIZE}

def test_get_stream_type_and_kwargs_raw_stream_by_line(mock_env):
    args = argparse.Namespace(prettify=False, stream=True)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, args)
    assert stream_class == RawStream
    assert stream_kwargs == {'chunk_size': RawStream.CHUNK_SIZE_BY_LINE}

def test_get_stream_type_and_kwargs_pretty_stream(mock_env, mock_plugin_manager, mocker):
    mocker.patch.object(mock_env, 'stdout_isatty', True)
    args = argparse.Namespace(prettify=['group1'], stream=True, style='default', json=False, format_options={})
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, args)
    assert stream_class == PrettyStream
    assert 'env' in stream_kwargs
    assert 'conversion' in stream_kwargs
    assert 'formatting' in stream_kwargs
    assert isinstance(stream_kwargs['formatting'], Formatting)

def test_get_stream_type_and_kwargs_buffered_pretty_stream(mock_env, mock_plugin_manager, mocker):
    mocker.patch.object(mock_env, 'stdout_isatty', True)
    args = argparse.Namespace(prettify=['group1'], stream=False, style='default', json=False, format_options={})
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, args)
    assert stream_class == BufferedPrettyStream
    assert 'env' in stream_kwargs
    assert 'conversion' in stream_kwargs
    assert 'formatting' in stream_kwargs
    assert isinstance(stream_kwargs['formatting'], Formatting)

def test_get_stream_type_and_kwargs_encoded_stream(mock_env, mocker):
    mocker.patch.object(mock_env, 'stdout_isatty', True)
    args = argparse.Namespace(prettify=False, stream=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, args)
    assert stream_class == EncodedStream
    assert stream_kwargs == {'env': mock_env}
