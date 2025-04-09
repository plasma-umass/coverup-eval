# file: lib/ansible/plugins/filter/mathstuff.py:179-186
# asked: {"lines": [179, 181, 182, 183, 184, 185, 186], "branches": []}
# gained: {"lines": [179, 181, 182, 183, 184, 185, 186], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.common.text import formatters
from ansible.module_utils._text import to_native
from ansible.plugins.filter.mathstuff import human_readable

def test_human_readable_valid_bytes(monkeypatch):
    def mock_bytes_to_human(size, isbits=False, unit=None):
        return "1.0 KiB"
    
    monkeypatch.setattr(formatters, "bytes_to_human", mock_bytes_to_human)
    result = human_readable(1024)
    assert result == "1.0 KiB"

def test_human_readable_valid_bits(monkeypatch):
    def mock_bytes_to_human(size, isbits=False, unit=None):
        return "8.0 Kibit"
    
    monkeypatch.setattr(formatters, "bytes_to_human", mock_bytes_to_human)
    result = human_readable(1024, isbits=True)
    assert result == "8.0 Kibit"

def test_human_readable_invalid_type(monkeypatch):
    def mock_bytes_to_human(size, isbits=False, unit=None):
        raise TypeError("Invalid type")
    
    monkeypatch.setattr(formatters, "bytes_to_human", mock_bytes_to_human)
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_readable("invalid")
    assert "human_readable() failed on bad input" in str(excinfo.value)

def test_human_readable_general_exception(monkeypatch):
    def mock_bytes_to_human(size, isbits=False, unit=None):
        raise Exception("General error")
    
    monkeypatch.setattr(formatters, "bytes_to_human", mock_bytes_to_human)
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_readable("invalid")
    assert "human_readable() can't interpret following string" in str(excinfo.value)
