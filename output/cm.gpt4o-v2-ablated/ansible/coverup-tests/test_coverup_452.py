# file: lib/ansible/module_utils/common/validation.py:543-551
# asked: {"lines": [548, 549, 550, 551], "branches": []}
# gained: {"lines": [548, 549, 550, 551], "branches": []}

import pytest
from ansible.module_utils.common.validation import check_type_bytes

def test_check_type_bytes_valid(monkeypatch):
    def mock_human_to_bytes(value):
        return 1024

    monkeypatch.setattr('ansible.module_utils.common.validation.human_to_bytes', mock_human_to_bytes)
    result = check_type_bytes("1KB")
    assert result == 1024

def test_check_type_bytes_invalid(monkeypatch):
    def mock_human_to_bytes(value):
        raise ValueError

    monkeypatch.setattr('ansible.module_utils.common.validation.human_to_bytes', mock_human_to_bytes)
    with pytest.raises(TypeError) as excinfo:
        check_type_bytes("invalid")
    assert str(excinfo.value) == "<class 'str'> cannot be converted to a Byte value"
