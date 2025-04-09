# file: lib/ansible/plugins/filter/core.py:558-566
# asked: {"lines": [558, 561, 562, 563, 564, 566], "branches": [[561, 562], [561, 563], [563, 564], [563, 566]]}
# gained: {"lines": [558, 561, 562, 563, 564, 566], "branches": [[561, 562], [561, 563], [563, 564], [563, 566]]}

import pytest
from ansible.plugins.filter.core import path_join
from ansible.errors import AnsibleFilterTypeError

def test_path_join_with_string():
    result = path_join("single_path")
    assert result == "single_path"

def test_path_join_with_sequence():
    result = path_join(["path", "to", "file"])
    assert result == "path/to/file"

def test_path_join_with_invalid_type():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        path_join(123)
    assert "|path_join expects string or sequence, got <class 'int'> instead." in str(excinfo.value)
