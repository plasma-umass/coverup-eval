# file lib/ansible/utils/py3compat.py:24-66
# lines [24, 25, 30, 31, 32, 33, 34, 37, 40, 42, 44, 45, 47, 48, 49, 50, 53, 54, 55, 56, 58, 59, 60, 62, 63, 65, 66]
# branches ['31->32', '31->33', '37->40', '37->42', '49->50', '49->53', '53->54', '53->56']

import os
import sys
import pytest
from collections.abc import MutableMapping
from ansible.utils.py3compat import to_text, to_bytes, PY3

class _TextEnviron(MutableMapping):
    """
    Utility class to return text strings from the environment instead of byte strings

    Mimics the behaviour of os.environ on Python3
    """
    def __init__(self, env=None, encoding=None):
        if env is None:
            env = os.environ
        self._raw_environ = env
        self._value_cache = {}
        # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding()
        # instead of utf-8
        if encoding is None:
            # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding()
            # instead of utf-8
            self.encoding = sys.getfilesystemencoding()
        else:
            self.encoding = encoding

    def __delitem__(self, key):
        del self._raw_environ[key]

    def __getitem__(self, key):
        value = self._raw_environ[key]
        if PY3:
            return value
        # Cache keys off of the undecoded values to handle any environment variables which change
        # during a run
        if value not in self._value_cache:
            self._value_cache[value] = to_text(value, encoding=self.encoding,
                                               nonstring='passthru', errors='surrogate_or_strict')
        return self._value_cache[value]

    def __setitem__(self, key, value):
        self._raw_environ[key] = value

    def __iter__(self):
        return self._raw_environ.__iter__()

    def __len__(self):
        return len(self._raw_environ)

@pytest.fixture
def mock_environ(mocker):
    original_environ = os.environ.copy()
    mocker.patch.dict(os.environ, {}, clear=True)
    yield
    os.environ.clear()
    os.environ.update(original_environ)

def test_text_environ(mock_environ):
    env = _TextEnviron()
    
    # Test __setitem__
    env['TEST_KEY'] = 'test_value'
    assert os.environ['TEST_KEY'] == 'test_value'
    
    # Test __getitem__
    assert env['TEST_KEY'] == 'test_value'
    
    # Test __delitem__
    del env['TEST_KEY']
    assert 'TEST_KEY' not in os.environ
    
    # Test __len__
    assert len(env) == len(os.environ)
    
    # Test __iter__
    env['TEST_KEY1'] = 'test_value1'
    env['TEST_KEY2'] = 'test_value2'
    keys = list(env)
    assert 'TEST_KEY1' in keys
    assert 'TEST_KEY2' in keys
