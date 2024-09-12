# file: lib/ansible/utils/py3compat.py:24-66
# asked: {"lines": [40, 45, 49, 50, 53, 54, 55, 56, 59, 60, 63, 66], "branches": [[31, 33], [37, 40], [49, 50], [49, 53], [53, 54], [53, 56]]}
# gained: {"lines": [40, 45, 49, 50, 59, 60, 63, 66], "branches": [[31, 33], [37, 40], [49, 50]]}

import os
import sys
import pytest
from ansible.module_utils.six import PY3
from ansible.module_utils._text import to_bytes, to_text
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.utils.py3compat import _TextEnviron

@pytest.fixture
def mock_environ(monkeypatch):
    mock_env = {}
    monkeypatch.setattr(os, 'environ', mock_env)
    return mock_env

def test_textenviron_init_default(mock_environ):
    env = _TextEnviron()
    assert env._raw_environ is mock_environ
    assert env.encoding == sys.getfilesystemencoding()

def test_textenviron_init_custom_env():
    custom_env = {'TEST': 'value'}
    env = _TextEnviron(env=custom_env)
    assert env._raw_environ is custom_env

def test_textenviron_init_custom_encoding():
    env = _TextEnviron(encoding='utf-8')
    assert env.encoding == 'utf-8'

def test_textenviron_delitem(mock_environ):
    mock_environ['TEST'] = 'value'
    env = _TextEnviron()
    del env['TEST']
    assert 'TEST' not in mock_environ

def test_textenviron_getitem_py3(mock_environ):
    mock_environ['TEST'] = 'value'
    env = _TextEnviron()
    if PY3:
        assert env['TEST'] == 'value'

def test_textenviron_getitem_cache(mock_environ):
    mock_environ['TEST'] = b'value'
    env = _TextEnviron()
    if not PY3:
        assert env['TEST'] == 'value'
        assert b'value' in env._value_cache

def test_textenviron_setitem(mock_environ):
    env = _TextEnviron()
    env['TEST'] = 'value'
    assert mock_environ['TEST'] == to_bytes('value', encoding=env.encoding, nonstring='strict', errors='surrogate_or_strict')

def test_textenviron_iter(mock_environ):
    mock_environ['TEST'] = 'value'
    env = _TextEnviron()
    keys = list(iter(env))
    assert 'TEST' in keys

def test_textenviron_len(mock_environ):
    mock_environ.clear()
    mock_environ['TEST'] = 'value'
    env = _TextEnviron()
    assert len(env) == 1
