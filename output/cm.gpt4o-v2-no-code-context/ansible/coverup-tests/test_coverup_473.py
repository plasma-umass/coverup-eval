# file: lib/ansible/plugins/filter/mathstuff.py:189-196
# asked: {"lines": [189, 191, 192, 193, 194, 195, 196], "branches": []}
# gained: {"lines": [189, 191, 192, 193, 194, 195, 196], "branches": []}

import pytest
from ansible.plugins.filter.mathstuff import human_to_bytes
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError

def test_human_to_bytes_valid_input(monkeypatch):
    def mock_human_to_bytes(size, default_unit, isbits):
        return 1024

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', mock_human_to_bytes)
    result = human_to_bytes('1KB')
    assert result == 1024

def test_human_to_bytes_type_error(monkeypatch):
    def mock_human_to_bytes(size, default_unit, isbits):
        raise TypeError("Invalid type")

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', mock_human_to_bytes)
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_to_bytes('invalid')
    assert "human_to_bytes() failed on bad input" in str(excinfo.value)

def test_human_to_bytes_general_exception(monkeypatch):
    def mock_human_to_bytes(size, default_unit, isbits):
        raise Exception("General error")

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.formatters.human_to_bytes', mock_human_to_bytes)
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_to_bytes('invalid')
    assert "human_to_bytes() can't interpret following string" in str(excinfo.value)
