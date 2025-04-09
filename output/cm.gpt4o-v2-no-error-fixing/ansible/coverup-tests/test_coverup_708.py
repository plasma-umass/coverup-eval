# file: lib/ansible/parsing/yaml/dumper.py:53-54
# asked: {"lines": [53, 54], "branches": []}
# gained: {"lines": [53, 54], "branches": []}

import pytest
import yaml
from ansible.module_utils.six import binary_type
from ansible.parsing.yaml.dumper import represent_binary

class DummyRepresenter:
    def represent_scalar(self, tag, value, style=None):
        return (tag, value, style)

def test_represent_binary(monkeypatch):
    def mock_represent_binary(self, data):
        return (self, data)

    monkeypatch.setattr(yaml.representer.SafeRepresenter, 'represent_binary', mock_represent_binary)

    dummy_representer = DummyRepresenter()
    data = b'test data'
    result = represent_binary(dummy_representer, data)
    
    assert result == (dummy_representer, binary_type(data))
