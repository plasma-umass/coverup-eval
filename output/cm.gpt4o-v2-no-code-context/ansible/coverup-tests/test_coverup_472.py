# file: lib/ansible/plugins/filter/mathstuff.py:179-186
# asked: {"lines": [179, 181, 182, 183, 184, 185, 186], "branches": []}
# gained: {"lines": [179, 181, 182, 183, 184, 185, 186], "branches": []}

import pytest
from ansible.plugins.filter.mathstuff import human_readable
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError
from ansible.module_utils._text import to_native

def test_human_readable_type_error(monkeypatch):
    def mock_bytes_to_human(size, isbits, unit):
        raise TypeError("mock type error")
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.formatters.bytes_to_human', mock_bytes_to_human)
    
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_readable("invalid_size")
    
    assert "human_readable() failed on bad input: mock type error" in str(excinfo.value)

def test_human_readable_general_exception(monkeypatch):
    def mock_bytes_to_human(size, isbits, unit):
        raise Exception("mock general exception")
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.formatters.bytes_to_human', mock_bytes_to_human)
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_readable("invalid_size")
    
    assert "human_readable() can't interpret following string: invalid_size" in str(excinfo.value)
