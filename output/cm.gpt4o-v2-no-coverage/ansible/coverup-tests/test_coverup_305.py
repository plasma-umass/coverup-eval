# file: lib/ansible/plugins/lookup/first_found.py:146-159
# asked: {"lines": [146, 149, 150, 151, 152, 153, 156, 157, 159], "branches": [[150, 151], [150, 156], [151, 152], [151, 153], [156, 157], [156, 159]]}
# gained: {"lines": [146, 149, 150, 151, 152, 153, 156, 157, 159], "branches": [[150, 151], [150, 156], [151, 152], [151, 153], [156, 157], [156, 159]]}

import pytest
from ansible.plugins.lookup.first_found import _split_on
from ansible.module_utils.six import string_types

def test_split_on_string():
    result = _split_on("a,b,c", ",")
    assert result == ["a", "b", "c"]

def test_split_on_string_with_multiple_splitters():
    result = _split_on("a,b;c", ",;")
    assert result == ["a", "b", "c"]

def test_split_on_list_of_strings():
    result = _split_on(["a,b", "c,d"], ",")
    assert result == ["a", "b", "c", "d"]

def test_split_on_list_of_strings_with_multiple_splitters():
    result = _split_on(["a,b", "c;d"], ",;")
    assert result == ["a", "b", "c", "d"]

def test_split_on_empty_string():
    result = _split_on("", ",")
    assert result == [""]

def test_split_on_empty_list():
    result = _split_on([], ",")
    assert result == []

def test_split_on_no_splitters():
    result = _split_on("abc", "")
    assert result == ["abc"]

def test_split_on_non_string_non_list():
    with pytest.raises(TypeError):
        _split_on(123, ",")

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Cleanup code to avoid state pollution
    yield
    monkeypatch.undo()
