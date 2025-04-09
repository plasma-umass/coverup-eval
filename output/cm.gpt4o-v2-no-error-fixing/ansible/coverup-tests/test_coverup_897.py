# file: lib/ansible/plugins/filter/core.py:47-54
# asked: {"lines": [49, 50, 51, 52, 53, 54], "branches": []}
# gained: {"lines": [49, 50, 51, 52, 53, 54], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_text
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml

from ansible.plugins.filter.core import to_yaml

def test_to_yaml_default_flow_style_none():
    data = {'key': 'value'}
    result = to_yaml(data)
    assert to_text(yaml.dump(data, Dumper=AnsibleDumper, allow_unicode=True, default_flow_style=None)) == result

def test_to_yaml_default_flow_style_true():
    data = {'key': 'value'}
    result = to_yaml(data, default_flow_style=True)
    assert to_text(yaml.dump(data, Dumper=AnsibleDumper, allow_unicode=True, default_flow_style=True)) == result

def test_to_yaml_exception_handling(mocker):
    data = {'key': 'value'}
    mocker.patch('yaml.dump', side_effect=Exception('test error'))
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_yaml(data)
    assert 'to_yaml - test error' in str(excinfo.value)
