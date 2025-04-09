# file: lib/ansible/plugins/filter/core.py:47-54
# asked: {"lines": [47, 49, 50, 51, 52, 53, 54], "branches": []}
# gained: {"lines": [47, 49, 50, 51, 52, 53, 54], "branches": []}

import pytest
import yaml
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_native, to_text
from ansible.plugins.filter.core import to_yaml
from unittest.mock import patch

def test_to_yaml_default_flow_style_none():
    data = {'key': 'value'}
    result = to_yaml(data)
    assert result == to_text(yaml.dump(data, Dumper=yaml.SafeDumper, allow_unicode=True, default_flow_style=None))

def test_to_yaml_with_default_flow_style():
    data = {'key': 'value'}
    result = to_yaml(data, default_flow_style=False)
    assert result == to_text(yaml.dump(data, Dumper=yaml.SafeDumper, allow_unicode=True, default_flow_style=False))

def test_to_yaml_exception_handling(monkeypatch):
    def mock_yaml_dump(*args, **kwargs):
        raise yaml.YAMLError("mock error")

    monkeypatch.setattr(yaml, 'dump', mock_yaml_dump)
    
    data = {'key': 'value'}
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_yaml(data)
    assert "to_yaml - mock error" in str(excinfo.value)
    assert isinstance(excinfo.value.orig_exc, yaml.YAMLError)
