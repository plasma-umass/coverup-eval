# file: lib/ansible/plugins/filter/core.py:57-63
# asked: {"lines": [57, 59, 60, 61, 62, 63], "branches": []}
# gained: {"lines": [57, 59, 60, 61, 62, 63], "branches": []}

import pytest
from ansible.plugins.filter.core import to_nice_yaml, AnsibleFilterError
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.module_utils._text import to_native, to_text
import yaml

def test_to_nice_yaml_success():
    data = {'key': 'value'}
    result = to_nice_yaml(data)
    expected = yaml.dump(data, Dumper=AnsibleDumper, indent=4, allow_unicode=True, default_flow_style=False)
    assert result == to_text(expected)

def test_to_nice_yaml_exception(monkeypatch):
    def mock_yaml_dump(*args, **kwargs):
        raise yaml.YAMLError("mock error")
    
    monkeypatch.setattr(yaml, 'dump', mock_yaml_dump)
    
    data = {'key': 'value'}
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_nice_yaml(data)
    
    assert "to_nice_yaml - mock error" in str(excinfo.value)
    assert isinstance(excinfo.value.orig_exc, yaml.YAMLError)
