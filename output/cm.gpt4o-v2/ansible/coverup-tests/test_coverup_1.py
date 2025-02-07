# file: lib/ansible/config/manager.py:49-158
# asked: {"lines": [49, 75, 76, 77, 78, 80, 81, 83, 84, 85, 87, 88, 90, 91, 93, 94, 95, 96, 97, 99, 100, 101, 103, 104, 106, 107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 121, 123, 124, 125, 127, 128, 130, 132, 133, 134, 136, 137, 139, 141, 142, 143, 145, 146, 147, 149, 152, 153, 155, 156, 158], "branches": [[77, 78], [77, 80], [80, 81], [80, 83], [83, 84], [83, 158], [84, 85], [84, 87], [87, 88], [87, 90], [90, 91], [90, 93], [93, 94], [93, 99], [94, 95], [94, 96], [96, 97], [96, 155], [99, 100], [99, 106], [100, 101], [100, 103], [103, 104], [103, 155], [106, 107], [106, 112], [107, 108], [107, 110], [112, 113], [112, 123], [113, 114], [113, 121], [115, 116], [115, 117], [123, 124], [123, 132], [124, 125], [124, 127], [127, 128], [127, 130], [132, 133], [132, 141], [133, 134], [133, 136], [136, 137], [136, 139], [141, 142], [141, 145], [142, 143], [142, 155], [145, 146], [145, 152], [146, 147], [146, 149], [152, 153], [152, 155], [155, 156], [155, 158]]}
# gained: {"lines": [49, 75, 76, 77, 80, 81, 83, 84, 85, 87, 88, 90, 91, 93, 94, 95, 96, 97, 99, 100, 101, 103, 104, 106, 107, 108, 110, 112, 113, 114, 115, 117, 118, 119, 121, 123, 124, 125, 127, 128, 130, 132, 133, 134, 136, 137, 139, 141, 142, 143, 145, 146, 147, 149, 152, 153, 155, 156, 158], "branches": [[77, 80], [80, 81], [80, 83], [83, 84], [84, 85], [84, 87], [87, 88], [87, 90], [90, 91], [90, 93], [93, 94], [93, 99], [94, 95], [94, 96], [96, 97], [99, 100], [99, 106], [100, 101], [100, 103], [103, 104], [103, 155], [106, 107], [106, 112], [107, 108], [107, 110], [112, 113], [112, 123], [113, 114], [113, 121], [115, 117], [123, 124], [123, 132], [124, 125], [124, 127], [127, 128], [127, 130], [132, 133], [132, 141], [133, 134], [133, 136], [136, 137], [136, 139], [141, 142], [141, 145], [142, 143], [142, 155], [145, 146], [145, 152], [146, 147], [146, 149], [152, 153], [155, 156], [155, 158]]}

import pytest
import os
import tempfile
from ansible.config.manager import ensure_type
from ansible.utils.path import cleanup_tmp_file

def test_ensure_type_boolean():
    assert ensure_type("True", "boolean") is True
    assert ensure_type("False", "boolean") is False

def test_ensure_type_integer():
    assert ensure_type("123", "integer") == 123

def test_ensure_type_float():
    assert ensure_type("123.45", "float") == 123.45

def test_ensure_type_list():
    assert ensure_type("a,b,c", "list") == ["a", "b", "c"]

def test_ensure_type_none():
    assert ensure_type("None", "none") is None

def test_ensure_type_path(tmpdir):
    path = tmpdir.mkdir("sub").strpath
    assert ensure_type(path, "path") == path

def test_ensure_type_tmppath(tmpdir):
    base_path = tmpdir.mkdir("base").strpath
    result_path = ensure_type(base_path, "tmppath")
    assert os.path.exists(result_path)
    cleanup_tmp_file(result_path)

def test_ensure_type_pathspec():
    assert ensure_type("/bin:/usr/bin", "pathspec") == ["/bin", "/usr/bin"]

def test_ensure_type_pathlist():
    assert ensure_type("/bin, /usr/bin", "pathlist") == ["/bin", "/usr/bin"]

def test_ensure_type_dict():
    assert ensure_type({"key": "value"}, "dict") == {"key": "value"}

def test_ensure_type_string():
    assert ensure_type(123, "string") == "123"

def test_ensure_type_default_string():
    assert ensure_type("test", None) == "test"

def test_ensure_type_invalid_list():
    with pytest.raises(ValueError, match='Invalid type provided for "list"'):
        ensure_type(123, "list")

def test_ensure_type_invalid_none():
    with pytest.raises(ValueError, match='Invalid type provided for "None"'):
        ensure_type("not_none", "none")

def test_ensure_type_invalid_path():
    with pytest.raises(ValueError, match='Invalid type provided for "path"'):
        ensure_type(123, "path")

def test_ensure_type_invalid_tmppath():
    with pytest.raises(ValueError, match='Invalid type provided for "temppath"'):
        ensure_type(123, "tmppath")

def test_ensure_type_invalid_pathspec():
    with pytest.raises(ValueError, match='Invalid type provided for "pathspec"'):
        ensure_type(123, "pathspec")

def test_ensure_type_invalid_pathlist():
    with pytest.raises(ValueError, match='Invalid type provided for "pathlist"'):
        ensure_type(123, "pathlist")

def test_ensure_type_invalid_dict():
    with pytest.raises(ValueError, match='Invalid type provided for "dictionary"'):
        ensure_type(123, "dict")

def test_ensure_type_invalid_string():
    with pytest.raises(ValueError, match='Invalid type provided for "string"'):
        ensure_type([], "string")
