# file: cookiecutter/replay.py:19-36
# asked: {"lines": [21, 22, 24, 25, 27, 28, 30, 31, 33, 35, 36], "branches": [[21, 22], [21, 24], [24, 25], [24, 27], [27, 28], [27, 30], [30, 31], [30, 33]]}
# gained: {"lines": [21, 22, 24, 25, 27, 28, 30, 31, 33, 35, 36], "branches": [[21, 22], [21, 24], [24, 25], [24, 27], [27, 28], [27, 30], [30, 31], [30, 33]]}

import pytest
import json
import os
from unittest.mock import patch, mock_open, call

# Assuming the functions make_sure_path_exists and get_file_name are imported from the module
from cookiecutter.replay import dump, make_sure_path_exists, get_file_name

def test_dump_creates_replay_dir(monkeypatch):
    def mock_make_sure_path_exists(path):
        return True

    monkeypatch.setattr('cookiecutter.replay.make_sure_path_exists', mock_make_sure_path_exists)
    monkeypatch.setattr('cookiecutter.replay.get_file_name', lambda x, y: 'dummy_path')

    context = {'cookiecutter': {}}
    dump('dummy_dir', 'template_name', context)

def test_dump_raises_ioerror(monkeypatch):
    def mock_make_sure_path_exists(path):
        return False

    monkeypatch.setattr('cookiecutter.replay.make_sure_path_exists', mock_make_sure_path_exists)

    with pytest.raises(IOError):
        dump('dummy_dir', 'template_name', {'cookiecutter': {}})

def test_dump_raises_typeerror_template_name():
    with pytest.raises(TypeError):
        dump('dummy_dir', 123, {'cookiecutter': {}})

def test_dump_raises_typeerror_context():
    with pytest.raises(TypeError):
        dump('dummy_dir', 'template_name', 'not_a_dict')

def test_dump_raises_valueerror_context():
    with pytest.raises(ValueError):
        dump('dummy_dir', 'template_name', {})

def test_dump_writes_to_file(monkeypatch):
    def mock_make_sure_path_exists(path):
        return True

    monkeypatch.setattr('cookiecutter.replay.make_sure_path_exists', mock_make_sure_path_exists)
    monkeypatch.setattr('cookiecutter.replay.get_file_name', lambda x, y: 'dummy_path')

    context = {'cookiecutter': {}}
    m = mock_open()
    with patch('builtins.open', m):
        dump('dummy_dir', 'template_name', context)

    m.assert_called_once_with('dummy_path', 'w')
    handle = m()
    handle.write.assert_has_calls([
        call('{'),
        call('\n  '),
        call('"cookiecutter"'),
        call(': '),
        call('{}'),
        call('\n'),
        call('}')
    ])
