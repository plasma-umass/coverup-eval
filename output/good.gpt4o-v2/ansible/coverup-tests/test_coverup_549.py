# file: lib/ansible/plugins/filter/core.py:47-54
# asked: {"lines": [47, 49, 50, 51, 52, 53, 54], "branches": []}
# gained: {"lines": [47, 49, 50, 51, 52, 53, 54], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_text
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml

# Import the function to be tested
from ansible.plugins.filter.core import to_yaml

def test_to_yaml_success():
    data = {'key': 'value'}
    result = to_yaml(data)
    expected = to_text(yaml.dump(data, Dumper=AnsibleDumper, allow_unicode=True, default_flow_style=None))
    assert expected == result

def test_to_yaml_with_default_flow_style():
    data = {'key': 'value'}
    result = to_yaml(data, default_flow_style=False)
    expected = to_text(yaml.dump(data, Dumper=AnsibleDumper, allow_unicode=True, default_flow_style=False))
    assert expected == result

def test_to_yaml_exception(mocker):
    data = {'key': 'value'}
    mocker.patch('yaml.dump', side_effect=Exception('test exception'))
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_yaml(data)
    assert 'to_yaml - test exception' in str(excinfo.value)
