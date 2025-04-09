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
    assert env._raw_environ is os.environ
    assert env.encoding == sys.getfilesystemencoding()

def test_textenviron_init_custom(mock_environ):
    custom_env = {'key': 'value'}
    custom_encoding = 'utf-8'
    env = _TextEnviron(env=custom_env, encoding=custom_encoding)
    assert env._raw_environ is custom_env
    assert env.encoding == custom_encoding

def test_textenviron_delitem(mock_environ):
    env = _TextEnviron()
    env._raw_environ['key'] = 'value'
    del env['key']
    assert 'key' not in env._raw_environ

def test_textenviron_getitem(mock_environ):
    env = _TextEnviron()
    env._raw_environ['key'] = 'value'
    assert env['key'] == 'value'

def test_textenviron_getitem_cache(mock_environ):
    env = _TextEnviron()
    env._raw_environ['key'] = b'value'
    if not PY3:
        assert env['key'] == 'value'
        assert b'value' in env._value_cache

def test_textenviron_setitem(mock_environ):
    env = _TextEnviron()
    env['key'] = 'value'
    assert env._raw_environ['key'] == to_bytes('value', encoding=env.encoding, nonstring='strict', errors='surrogate_or_strict')

def test_textenviron_iter(mock_environ):
    env = _TextEnviron()
    env._raw_environ['key'] = 'value'
    keys = list(iter(env))
    assert 'key' in keys

def test_textenviron_len(mock_environ):
    env = _TextEnviron()
    env._raw_environ.clear()  # Ensure the environment is empty
    env._raw_environ['key'] = 'value'
    assert len(env) == 1
