# file: lib/ansible/parsing/yaml/dumper.py:49-50
# asked: {"lines": [49, 50], "branches": []}
# gained: {"lines": [49, 50], "branches": []}

import pytest
import yaml
from ansible.module_utils.six import text_type
from ansible.parsing.yaml.dumper import represent_unicode

class DummyRepresenter:
    def represent_scalar(self, tag, value):
        return (tag, value)

def test_represent_unicode(monkeypatch):
    def mock_represent_str(self, data):
        return self.represent_scalar('tag:yaml.org,2002:str', data)
    
    monkeypatch.setattr(yaml.representer.SafeRepresenter, 'represent_str', mock_represent_str)
    
    dummy_representer = DummyRepresenter()
    result = represent_unicode(dummy_representer, 'test_unicode')
    
    assert result == ('tag:yaml.org,2002:str', text_type('test_unicode'))
