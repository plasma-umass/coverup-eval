# file: lib/ansible/constants.py:48-60
# asked: {"lines": [48, 49, 50, 51, 52, 54, 55, 56, 58, 59, 60], "branches": []}
# gained: {"lines": [48, 49, 50, 51, 52, 54, 55, 56, 58, 59, 60], "branches": []}

import pytest
from ansible.constants import _DeprecatedSequenceConstant

def _deprecated(msg, version):
    # Mock function to simulate deprecation warning
    print(f"Deprecated: {msg} (version {version})")

def test_deprecated_sequence_constant_len(monkeypatch):
    # Mock the _deprecated function
    monkeypatch.setattr('ansible.constants._deprecated', _deprecated)
    
    value = [1, 2, 3]
    msg = "This sequence is deprecated"
    version = "2.0"
    
    deprecated_seq = _DeprecatedSequenceConstant(value, msg, version)
    
    assert len(deprecated_seq) == 3

def test_deprecated_sequence_constant_getitem(monkeypatch):
    # Mock the _deprecated function
    monkeypatch.setattr('ansible.constants._deprecated', _deprecated)
    
    value = [1, 2, 3]
    msg = "This sequence is deprecated"
    version = "2.0"
    
    deprecated_seq = _DeprecatedSequenceConstant(value, msg, version)
    
    assert deprecated_seq[0] == 1
    assert deprecated_seq[1] == 2
    assert deprecated_seq[2] == 3
