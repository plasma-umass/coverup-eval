# file: pysnooper/tracer.py:49-108
# asked: {"lines": [62, 63, 64, 65, 66, 67, 71, 72, 73, 74, 75, 76, 77, 78, 79, 84, 85, 89, 101, 102], "branches": [[61, 62], [66, 67], [66, 68], [68, 86], [70, 71], [86, 89], [94, 106], [100, 101]]}
# gained: {"lines": [62, 63, 64, 65, 66, 67, 71, 72, 73, 74, 75, 76, 77, 84, 85, 89, 101, 102], "branches": [[61, 62], [66, 67], [66, 68], [68, 86], [70, 71], [86, 89], [94, 106], [100, 101]]}

import pytest
import re
from unittest.mock import Mock, patch, mock_open
from pysnooper.tracer import get_path_and_source_from_frame, UnavailableSource, source_and_path_cache
from pysnooper import utils, pycompat

ipython_filename_pattern = re.compile('^<ipython-input-([0-9]+)-.*>$')

def test_get_path_and_source_from_frame_loader_get_source(monkeypatch):
    frame = Mock()
    frame.f_globals = {'__name__': 'test_module', '__loader__': Mock()}
    frame.f_code.co_filename = 'test_file.py'
    loader = frame.f_globals['__loader__']
    loader.get_source = Mock(return_value="print('hello world')")

    result = get_path_and_source_from_frame(frame)
    assert result[1] == ["print('hello world')"]

def test_get_path_and_source_from_frame_loader_import_error(monkeypatch):
    frame = Mock()
    frame.f_globals = {'__name__': 'test_module', '__loader__': Mock()}
    frame.f_code.co_filename = 'test_file.py'
    loader = frame.f_globals['__loader__']
    loader.get_source = Mock(side_effect=ImportError)

    result = get_path_and_source_from_frame(frame)
    assert isinstance(result[1], UnavailableSource)

def test_get_path_and_source_from_frame_ipython(monkeypatch):
    frame = Mock()
    frame.f_globals = {'__name__': 'test_module'}
    frame.f_code.co_filename = '<ipython-input-1-test>'
    ipython_mock = Mock()
    ipython_mock.get_ipython().history_manager.get_range.return_value = [(None, None, "print('hello world')")]
    monkeypatch.setattr('IPython.get_ipython', ipython_mock.get_ipython)

    result = get_path_and_source_from_frame(frame)
    assert result[1] == ["print('hello world')"]

def test_get_path_and_source_from_frame_file_reading(monkeypatch):
    frame = Mock()
    frame.f_globals = {'__name__': 'test_module'}
    frame.f_code.co_filename = 'test_file.py'
    mock_file_data = b"print('hello world')\n# coding: utf-8"
    monkeypatch.setattr('builtins.open', mock_open(read_data=mock_file_data))

    result = get_path_and_source_from_frame(frame)
    assert result[1] == ["print('hello world')", "# coding: utf-8"]

def test_get_path_and_source_from_frame_file_reading_error(monkeypatch):
    frame = Mock()
    frame.f_globals = {'__name__': 'test_module'}
    frame.f_code.co_filename = 'test_file.py'
    monkeypatch.setattr('builtins.open', mock_open(read_data=b""))
    monkeypatch.setattr('pysnooper.utils.file_reading_errors', (OSError, IOError))

    result = get_path_and_source_from_frame(frame)
    assert isinstance(result[1], UnavailableSource)

def test_get_path_and_source_from_frame_encoding_detection(monkeypatch):
    frame = Mock()
    frame.f_globals = {'__name__': 'test_module'}
    frame.f_code.co_filename = 'test_file.py'
    mock_file_data = b"# coding: latin-1\nprint('hello world')"
    monkeypatch.setattr('builtins.open', mock_open(read_data=mock_file_data))

    result = get_path_and_source_from_frame(frame)
    assert result[1] == ["# coding: latin-1", "print('hello world')"]

def test_get_path_and_source_from_frame_cache(monkeypatch):
    frame = Mock()
    frame.f_globals = {'__name__': 'test_module'}
    frame.f_code.co_filename = 'test_file.py'
    cache_key = ('test_module', 'test_file.py')
    source_and_path_cache[cache_key] = ('test_file.py', ["print('hello world')"])

    result = get_path_and_source_from_frame(frame)
    assert result == ('test_file.py', ["print('hello world')"])
