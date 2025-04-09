# file: lib/ansible/config/manager.py:49-158
# asked: {"lines": [49, 75, 76, 77, 78, 80, 81, 83, 84, 85, 87, 88, 90, 91, 93, 94, 95, 96, 97, 99, 100, 101, 103, 104, 106, 107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 121, 123, 124, 125, 127, 128, 130, 132, 133, 134, 136, 137, 139, 141, 142, 143, 145, 146, 147, 149, 152, 153, 155, 156, 158], "branches": [[77, 78], [77, 80], [80, 81], [80, 83], [83, 84], [83, 158], [84, 85], [84, 87], [87, 88], [87, 90], [90, 91], [90, 93], [93, 94], [93, 99], [94, 95], [94, 96], [96, 97], [96, 155], [99, 100], [99, 106], [100, 101], [100, 103], [103, 104], [103, 155], [106, 107], [106, 112], [107, 108], [107, 110], [112, 113], [112, 123], [113, 114], [113, 121], [115, 116], [115, 117], [123, 124], [123, 132], [124, 125], [124, 127], [127, 128], [127, 130], [132, 133], [132, 141], [133, 134], [133, 136], [136, 137], [136, 139], [141, 142], [141, 145], [142, 143], [142, 155], [145, 146], [145, 152], [146, 147], [146, 149], [152, 153], [152, 155], [155, 156], [155, 158]]}
# gained: {"lines": [49, 75, 76, 77, 80, 81, 83, 84, 85, 87, 88, 90, 91, 93, 94, 95, 96, 97, 99, 100, 101, 103, 104, 106, 107, 108, 112, 113, 114, 115, 117, 118, 119, 123, 124, 125, 127, 128, 132, 133, 134, 136, 137, 141, 142, 143, 145, 146, 147, 149, 155, 156, 158], "branches": [[77, 80], [80, 81], [83, 84], [84, 85], [84, 87], [87, 88], [87, 90], [90, 91], [90, 93], [93, 94], [93, 99], [94, 95], [94, 96], [96, 97], [99, 100], [99, 106], [100, 101], [100, 103], [103, 104], [103, 155], [106, 107], [106, 112], [107, 108], [112, 113], [112, 123], [113, 114], [115, 117], [123, 124], [123, 132], [124, 125], [127, 128], [132, 133], [132, 141], [133, 134], [136, 137], [141, 142], [141, 145], [142, 143], [142, 155], [145, 146], [146, 147], [146, 149], [155, 156], [155, 158]]}

import pytest
import os
import tempfile
from ansible.config.manager import ensure_type
from ansible.module_utils.six import string_types
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.utils.path import cleanup_tmp_file

def test_ensure_type_boolean():
    assert ensure_type("true", "boolean") is True
    assert ensure_type("false", "boolean") is False

def test_ensure_type_integer():
    assert ensure_type("123", "integer") == 123
    with pytest.raises(ValueError):
        ensure_type("abc", "integer")

def test_ensure_type_float():
    assert ensure_type("123.45", "float") == 123.45
    with pytest.raises(ValueError):
        ensure_type("abc", "float")

def test_ensure_type_list():
    assert ensure_type("a,b,c", "list") == ["a", "b", "c"]
    with pytest.raises(ValueError):
        ensure_type(123, "list")

def test_ensure_type_none():
    assert ensure_type("None", "none") is None
    with pytest.raises(ValueError):
        ensure_type("abc", "none")

def test_ensure_type_path(monkeypatch):
    def mock_resolve_path(path, basedir=None):
        return "/mocked/path"
    monkeypatch.setattr("ansible.config.manager.resolve_path", mock_resolve_path)
    assert ensure_type("~/test", "path") == "/mocked/path"

def test_ensure_type_tmppath(monkeypatch):
    def mock_resolve_path(path, basedir=None):
        return tempfile.gettempdir()
    monkeypatch.setattr("ansible.config.manager.resolve_path", mock_resolve_path)
    tmp_path = ensure_type("~/test", "tmppath")
    assert os.path.exists(tmp_path)
    cleanup_tmp_file(tmp_path)

def test_ensure_type_pathspec(monkeypatch):
    def mock_resolve_path(path, basedir=None):
        return "/mocked/path"
    monkeypatch.setattr("ansible.config.manager.resolve_path", mock_resolve_path)
    assert ensure_type("~/test:~/test2", "pathspec") == ["/mocked/path", "/mocked/path"]

def test_ensure_type_pathlist(monkeypatch):
    def mock_resolve_path(path, basedir=None):
        return "/mocked/path"
    monkeypatch.setattr("ansible.config.manager.resolve_path", mock_resolve_path)
    assert ensure_type("a,b,c", "pathlist") == ["/mocked/path", "/mocked/path", "/mocked/path"]

def test_ensure_type_dict():
    assert ensure_type({"key": "value"}, "dict") == {"key": "value"}
    with pytest.raises(ValueError):
        ensure_type("not a dict", "dict")

def test_ensure_type_string():
    assert ensure_type(123, "string") == "123"
    assert ensure_type(AnsibleVaultEncryptedUnicode("vaulted"), "string") == "vaulted"
    with pytest.raises(ValueError):
        ensure_type([], "string")
