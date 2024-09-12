# file: httpie/output/writer.py:121-156
# asked: {"lines": [121, 128, 129, 130, 131, 132, 133, 134, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 151, 152, 153, 156], "branches": [[128, 129], [128, 137], [137, 138], [137, 151]]}
# gained: {"lines": [121, 128, 129, 130, 131, 132, 133, 134, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 151, 152, 153, 156], "branches": [[128, 129], [128, 137], [137, 138], [137, 151]]}

import pytest
import argparse
from unittest.mock import Mock, patch
from httpie.output.writer import get_stream_type_and_kwargs
from httpie.context import Environment
from httpie.output.streams import RawStream, PrettyStream, BufferedPrettyStream, EncodedStream
from httpie.output.processing import Conversion, Formatting

@pytest.fixture
def mock_env():
    env = Mock(spec=Environment)
    env.stdout_isatty = True
    env.stdout_encoding = 'utf-8'
    return env

@pytest.fixture
def mock_args():
    args = Mock(spec=argparse.Namespace)
    args.prettify = None
    args.stream = False
    args.style = 'default'
    args.json = False
    args.format_options = {}
    return args

def test_get_stream_type_and_kwargs_raw_stream(mock_env, mock_args):
    mock_env.stdout_isatty = False
    mock_args.prettify = None
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, mock_args)
    assert stream_class == RawStream
    assert stream_kwargs == {'chunk_size': RawStream.CHUNK_SIZE}

def test_get_stream_type_and_kwargs_raw_stream_by_line(mock_env, mock_args):
    mock_env.stdout_isatty = False
    mock_args.prettify = None
    mock_args.stream = True
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, mock_args)
    assert stream_class == RawStream
    assert stream_kwargs == {'chunk_size': RawStream.CHUNK_SIZE_BY_LINE}

@patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'group1': [], 'group2': []})
def test_get_stream_type_and_kwargs_pretty_stream(mock_get_formatters_grouped, mock_env, mock_args):
    mock_args.prettify = ['group1']
    mock_args.stream = True
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, mock_args)
    assert stream_class == PrettyStream
    assert isinstance(stream_kwargs['conversion'], Conversion)
    assert isinstance(stream_kwargs['formatting'], Formatting)
    assert stream_kwargs['env'] == mock_env

@patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'group1': [], 'group2': []})
def test_get_stream_type_and_kwargs_buffered_pretty_stream(mock_get_formatters_grouped, mock_env, mock_args):
    mock_args.prettify = ['group1']
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, mock_args)
    assert stream_class == BufferedPrettyStream
    assert isinstance(stream_kwargs['conversion'], Conversion)
    assert isinstance(stream_kwargs['formatting'], Formatting)
    assert stream_kwargs['env'] == mock_env

def test_get_stream_type_and_kwargs_encoded_stream(mock_env, mock_args):
    stream_class, stream_kwargs = get_stream_type_and_kwargs(mock_env, mock_args)
    assert stream_class == EncodedStream
    assert stream_kwargs == {'env': mock_env}
