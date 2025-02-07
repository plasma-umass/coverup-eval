# file: lib/ansible/parsing/yaml/dumper.py:53-54
# asked: {"lines": [54], "branches": []}
# gained: {"lines": [54], "branches": []}

import pytest
import yaml
import base64
from ansible.module_utils.six import binary_type
from ansible.parsing.yaml.dumper import represent_binary

class DummyRepresenter:
    def represent_scalar(self, tag, value, style=None):
        return (tag, value, style)

def test_represent_binary(monkeypatch):
    dummy_representer = DummyRepresenter()
    
    def mock_represent_binary(self, data):
        if isinstance(data, binary_type):
            if hasattr(base64, 'encodebytes'):
                data = base64.encodebytes(data).decode('ascii')
            else:
                data = base64.encodestring(data).decode('ascii')
            return dummy_representer.represent_scalar('tag:yaml.org,2002:binary', data, style='|')
        return yaml.representer.SafeRepresenter.represent_binary(dummy_representer, data)
    
    monkeypatch.setattr(yaml.representer.SafeRepresenter, 'represent_binary', mock_represent_binary)
    
    data = b"test binary data"
    result = represent_binary(dummy_representer, data)
    
    assert result == ('tag:yaml.org,2002:binary', 'dGVzdCBiaW5hcnkgZGF0YQ==\n', '|')
