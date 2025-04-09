# file: lib/ansible/module_utils/common/validation.py:554-564
# asked: {"lines": [554, 561, 562, 563, 564], "branches": []}
# gained: {"lines": [554, 561, 562, 563, 564], "branches": []}

import pytest
from ansible.module_utils.common.validation import check_type_bits

def test_check_type_bits_valid(monkeypatch):
    def mock_human_to_bytes(value, isbits):
        return 1048576

    monkeypatch.setattr('ansible.module_utils.common.validation.human_to_bytes', mock_human_to_bytes)
    result = check_type_bits('1Mb')
    assert result == 1048576

def test_check_type_bits_invalid(monkeypatch):
    def mock_human_to_bytes(value, isbits):
        raise ValueError

    monkeypatch.setattr('ansible.module_utils.common.validation.human_to_bytes', mock_human_to_bytes)
    with pytest.raises(TypeError) as excinfo:
        check_type_bits('invalid')
    assert str(excinfo.value) == "<class 'str'> cannot be converted to a Bit value"
