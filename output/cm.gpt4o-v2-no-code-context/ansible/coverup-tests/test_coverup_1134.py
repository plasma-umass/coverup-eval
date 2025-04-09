# file: lib/ansible/config/manager.py:49-158
# asked: {"lines": [78, 97, 100, 101, 103, 104, 110, 116, 121, 130, 139, 143, 149, 156], "branches": [[77, 78], [96, 97], [99, 100], [100, 101], [100, 103], [103, 104], [103, 155], [107, 110], [113, 121], [115, 116], [124, 127], [127, 130], [133, 136], [136, 139], [142, 143], [146, 149], [155, 156]]}
# gained: {"lines": [78, 100, 101, 103, 104, 130, 139, 143, 149, 156], "branches": [[77, 78], [99, 100], [100, 101], [100, 103], [103, 104], [103, 155], [124, 127], [127, 130], [133, 136], [136, 139], [142, 143], [146, 149], [155, 156]]}

import os
import pytest
import tempfile
import atexit
from ansible.config.manager import ensure_type
from ansible.module_utils._text import to_bytes, to_text
from ansible.module_utils.common._collections_compat import Mapping, Sequence
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def mock_os_path_isabs(monkeypatch):
    def mock_isabs(path):
        return True
    monkeypatch.setattr(os.path, 'isabs', mock_isabs)

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_exists(path):
        return True
    monkeypatch.setattr(os.path, 'exists', mock_exists)

@pytest.fixture
def mock_tempfile_mkdtemp(monkeypatch):
    def mock_mkdtemp(prefix, dir):
        return os.path.join(dir, prefix + 'mocked')
    monkeypatch.setattr(tempfile, 'mkdtemp', mock_mkdtemp)

@pytest.fixture
def mock_atexit_register(monkeypatch):
    def mock_register(func, *args, **kwargs):
        pass
    monkeypatch.setattr(atexit, 'register', mock_register)

@pytest.fixture
def mock_resolve_path(monkeypatch):
    def mock_resolve_path(value, basedir=None):
        return os.path.join(basedir, value) if basedir else value
    monkeypatch.setattr('ansible.config.manager.resolve_path', mock_resolve_path)

@pytest.fixture
def mock_makedirs_safe(monkeypatch):
    def mock_makedirs_safe(path, mode):
        pass
    monkeypatch.setattr('ansible.config.manager.makedirs_safe', mock_makedirs_safe)

def test_ensure_type_path(mock_os_path_isabs, mock_os_path_exists, mock_resolve_path):
    origin = '/mock/origin'
    value = '~/mock/path'
    value_type = 'path'
    result = ensure_type(value, value_type, origin)
    assert result == os.path.join(origin, value)

def test_ensure_type_tmppath(mock_os_path_isabs, mock_os_path_exists, mock_tempfile_mkdtemp, mock_atexit_register, mock_resolve_path, mock_makedirs_safe):
    origin = '/mock/origin'
    value = '/mock/tmp'
    value_type = 'tmppath'
    result = ensure_type(value, value_type, origin)
    assert result == os.path.join(value, 'ansible-local-%s' % os.getpid() + 'mocked')

def test_ensure_type_none():
    value = "None"
    value_type = 'none'
    result = ensure_type(value, value_type)
    assert result is None

def test_ensure_type_none_invalid():
    value = "not_none"
    value_type = 'none'
    with pytest.raises(ValueError):
        ensure_type(value, value_type)

def test_ensure_type_pathspec(mock_os_path_isabs, mock_os_path_exists, mock_resolve_path):
    origin = '/mock/origin'
    value = '~/mock/path:~/mock/another_path'
    value_type = 'pathspec'
    result = ensure_type(value, value_type, origin)
    expected = [os.path.join(origin, x) for x in value.split(os.pathsep)]
    assert result == expected

def test_ensure_type_pathspec_invalid():
    value = 12345
    value_type = 'pathspec'
    with pytest.raises(ValueError):
        ensure_type(value, value_type)

def test_ensure_type_pathlist(mock_os_path_isabs, mock_os_path_exists, mock_resolve_path):
    origin = '/mock/origin'
    value = '~/mock/path,~/mock/another_path'
    value_type = 'pathlist'
    result = ensure_type(value, value_type, origin)
    expected = [os.path.join(origin, x.strip()) for x in value.split(',')]
    assert result == expected

def test_ensure_type_pathlist_invalid():
    value = 12345
    value_type = 'pathlist'
    with pytest.raises(ValueError):
        ensure_type(value, value_type)

def test_ensure_type_dictionary():
    value = {"key": "value"}
    value_type = 'dictionary'
    result = ensure_type(value, value_type)
    assert result == value

def test_ensure_type_dictionary_invalid():
    value = ["not", "a", "dict"]
    value_type = 'dictionary'
    with pytest.raises(ValueError):
        ensure_type(value, value_type)

def test_ensure_type_string():
    value = 12345
    value_type = 'string'
    result = ensure_type(value, value_type)
    assert result == to_text(value, errors='surrogate_or_strict')

def test_ensure_type_string_invalid():
    value = object()
    value_type = 'string'
    with pytest.raises(ValueError):
        ensure_type(value, value_type)
