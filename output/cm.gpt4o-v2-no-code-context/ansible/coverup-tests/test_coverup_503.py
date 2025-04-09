# file: lib/ansible/plugins/filter/core.py:57-63
# asked: {"lines": [57, 59, 60, 61, 62, 63], "branches": []}
# gained: {"lines": [57, 59, 60, 61, 62, 63], "branches": []}

import pytest
from ansible.plugins.filter.core import to_nice_yaml, AnsibleFilterError
from ansible.module_utils._text import to_text
import yaml

def test_to_nice_yaml_success():
    data = {'key': 'value'}
    result = to_nice_yaml(data)
    assert result == to_text(yaml.dump(data, Dumper=yaml.SafeDumper, indent=4, allow_unicode=True, default_flow_style=False))

def test_to_nice_yaml_exception(mocker):
    mocker.patch('yaml.dump', side_effect=Exception('test exception'))
    data = {'key': 'value'}
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_nice_yaml(data)
    assert 'to_nice_yaml - test exception' in str(excinfo.value)
