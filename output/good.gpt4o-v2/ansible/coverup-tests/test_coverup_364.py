# file: lib/ansible/constants.py:48-60
# asked: {"lines": [48, 49, 50, 51, 52, 54, 55, 56, 58, 59, 60], "branches": []}
# gained: {"lines": [48, 49, 50, 51, 52, 54, 55, 56, 58, 59, 60], "branches": []}

import pytest
from ansible.constants import _DeprecatedSequenceConstant

def _deprecated(msg, version):
    # Mock implementation of the _deprecated function
    pass

@pytest.fixture
def deprecated_sequence_constant():
    value = [1, 2, 3]
    msg = "This is deprecated"
    version = "2.0"
    return _DeprecatedSequenceConstant(value, msg, version)

def test_len_deprecated_sequence_constant(monkeypatch, deprecated_sequence_constant):
    def mock_deprecated(msg, version):
        assert msg == "This is deprecated"
        assert version == "2.0"
    
    monkeypatch.setattr("ansible.constants._deprecated", mock_deprecated)
    
    assert len(deprecated_sequence_constant) == 3

def test_getitem_deprecated_sequence_constant(monkeypatch, deprecated_sequence_constant):
    def mock_deprecated(msg, version):
        assert msg == "This is deprecated"
        assert version == "2.0"
    
    monkeypatch.setattr("ansible.constants._deprecated", mock_deprecated)
    
    assert deprecated_sequence_constant[0] == 1
    assert deprecated_sequence_constant[1] == 2
    assert deprecated_sequence_constant[2] == 3
