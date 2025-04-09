# file: lib/ansible/plugins/filter/core.py:47-54
# asked: {"lines": [49, 50, 51, 52, 53, 54], "branches": []}
# gained: {"lines": [49, 50, 51, 52, 53, 54], "branches": []}

import pytest
import yaml
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_native, to_text
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.filter.core import to_yaml

def test_to_yaml_success():
    data = {'key': 'value'}
    result = to_yaml(data)
    assert isinstance(result, str)
    assert 'key' in result
    assert 'value' in result

def test_to_yaml_with_default_flow_style():
    data = {'key': 'value'}
    result = to_yaml(data, default_flow_style=True)
    assert isinstance(result, str)
    assert '{key: value}' in result

def test_to_yaml_exception(mocker):
    mocker.patch('yaml.dump', side_effect=Exception('test error'))
    data = {'key': 'value'}
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_yaml(data)
    assert 'to_yaml - test error' in str(excinfo.value)
    assert isinstance(excinfo.value.orig_exc, Exception)
