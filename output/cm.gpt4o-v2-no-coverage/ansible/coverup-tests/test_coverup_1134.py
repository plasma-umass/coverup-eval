# file: lib/ansible/config/manager.py:49-158
# asked: {"lines": [78, 110, 116, 121, 130, 139], "branches": [[77, 78], [107, 110], [113, 121], [115, 116], [124, 127], [127, 130], [133, 136], [136, 139]]}
# gained: {"lines": [110, 116, 130, 139], "branches": [[107, 110], [115, 116], [124, 127], [127, 130], [133, 136], [136, 139]]}

import pytest
import os
import tempfile
from ansible.config.manager import ensure_type
from ansible.module_utils._text import to_text, to_bytes, to_native
from ansible.module_utils.common._collections_compat import Mapping, Sequence
from ansible.module_utils.six import string_types
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.parsing.quoting import unquote
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.path import cleanup_tmp_file, makedirs_safe

def test_ensure_type_boolean():
    assert ensure_type("yes", "boolean") is True
    assert ensure_type("no", "boolean") is False
    assert ensure_type("true", "bool") is True
    assert ensure_type("false", "bool") is False

def test_ensure_type_integer():
    assert ensure_type("42", "integer") == 42
    assert ensure_type("0", "int") == 0

def test_ensure_type_float():
    assert ensure_type("3.14", "float") == 3.14

def test_ensure_type_list():
    assert ensure_type("a,b,c", "list") == ["a", "b", "c"]
    assert ensure_type(["a", "b", "c"], "list") == ["a", "b", "c"]

def test_ensure_type_none():
    assert ensure_type("None", "none") is None
    with pytest.raises(ValueError):
        ensure_type("not_none", "none")

def test_ensure_type_path(monkeypatch):
    def mock_resolve_path(value, basedir=None):
        return value

    monkeypatch.setattr("ansible.config.manager.resolve_path", mock_resolve_path)
    assert ensure_type("~/path", "path") == "~/path"
    with pytest.raises(ValueError):
        ensure_type(123, "path")

def test_ensure_type_tmppath(monkeypatch):
    def mock_resolve_path(value, basedir=None):
        return value

    monkeypatch.setattr("ansible.config.manager.resolve_path", mock_resolve_path)
    temp_dir = tempfile.mkdtemp()
    monkeypatch.setattr(tempfile, "mkdtemp", lambda prefix, dir: temp_dir)
    result = ensure_type("~/path", "tmppath")
    assert result == temp_dir
    assert os.path.exists(result)
    cleanup_tmp_file(result)

def test_ensure_type_pathspec(monkeypatch):
    def mock_resolve_path(value, basedir=None):
        return value

    monkeypatch.setattr("ansible.config.manager.resolve_path", mock_resolve_path)
    assert ensure_type("~/path:~/another_path", "pathspec") == ["~/path", "~/another_path"]
    with pytest.raises(ValueError):
        ensure_type(123, "pathspec")

def test_ensure_type_pathlist(monkeypatch):
    def mock_resolve_path(value, basedir=None):
        return value

    monkeypatch.setattr("ansible.config.manager.resolve_path", mock_resolve_path)
    assert ensure_type("path1,path2", "pathlist") == ["path1", "path2"]
    with pytest.raises(ValueError):
        ensure_type(123, "pathlist")

def test_ensure_type_dict():
    assert ensure_type({"key": "value"}, "dict") == {"key": "value"}
    with pytest.raises(ValueError):
        ensure_type(["not", "a", "dict"], "dict")

def test_ensure_type_string():
    assert ensure_type(42, "string") == "42"
    assert ensure_type(True, "str") == "True"
    with pytest.raises(ValueError):
        ensure_type([], "string")

def test_ensure_type_default():
    assert ensure_type("text", None) == "text"
    assert ensure_type(AnsibleVaultEncryptedUnicode("encrypted"), None) == "encrypted"
