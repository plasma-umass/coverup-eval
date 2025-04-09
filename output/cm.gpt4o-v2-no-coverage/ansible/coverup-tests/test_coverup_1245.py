# file: lib/ansible/parsing/yaml/dumper.py:49-50
# asked: {"lines": [50], "branches": []}
# gained: {"lines": [50], "branches": []}

import pytest
import yaml
from ansible.module_utils.six import text_type
from ansible.parsing.yaml.dumper import represent_unicode

class MockSafeRepresenter:
    def represent_scalar(self, tag, value):
        return (tag, value)

def test_represent_unicode():
    mock_representer = MockSafeRepresenter()
    data = "test string"
    
    result = represent_unicode(mock_representer, data)
    
    assert result == ('tag:yaml.org,2002:str', text_type(data))

    # Clean up
    del mock_representer
    del data
    del result
