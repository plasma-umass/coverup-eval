# file: lib/ansible/parsing/yaml/dumper.py:53-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest
import yaml
from ansible.parsing.yaml.dumper import represent_binary
from ansible.module_utils.six import binary_type

class MockSafeRepresenter:
    def represent_scalar(self, tag, value, style=None):
        return (tag, value, style)

def test_represent_binary(monkeypatch):
    # Arrange
    mock_representer = MockSafeRepresenter()
    data = b"test data"
    
    # Act
    result = represent_binary(mock_representer, data)
    
    # Assert
    assert result == ('tag:yaml.org,2002:binary', 'dGVzdCBkYXRh\n', '|')
