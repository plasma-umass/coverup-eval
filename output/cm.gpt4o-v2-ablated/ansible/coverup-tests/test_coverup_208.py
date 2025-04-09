# file: lib/ansible/plugins/filter/mathstuff.py:179-186
# asked: {"lines": [179, 181, 182, 183, 184, 185, 186], "branches": []}
# gained: {"lines": [179, 181, 182, 183, 184, 185, 186], "branches": []}

import pytest
from ansible.plugins.filter.mathstuff import human_readable
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError
from ansible.module_utils._text import to_native

class MockFormatters:
    @staticmethod
    def bytes_to_human(size, isbits, unit):
        if isinstance(size, (int, float)):
            return f"{size} human-readable"
        else:
            raise TypeError("Invalid type for size")

@pytest.fixture
def mock_formatters(monkeypatch):
    monkeypatch.setattr("ansible.plugins.filter.mathstuff.formatters", MockFormatters)

def test_human_readable_valid_input(mock_formatters):
    result = human_readable(1024)
    assert result == "1024 human-readable"

def test_human_readable_invalid_type(mock_formatters):
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_readable("invalid")
    assert "human_readable() failed on bad input" in str(excinfo.value)

def test_human_readable_unexpected_exception(monkeypatch):
    def mock_bytes_to_human(size, isbits, unit):
        raise Exception("Unexpected error")
    
    monkeypatch.setattr("ansible.plugins.filter.mathstuff.formatters.bytes_to_human", mock_bytes_to_human)
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_readable(1024)
    assert "human_readable() can't interpret following string" in str(excinfo.value)
