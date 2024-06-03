# file lib/ansible/plugins/filter/core.py:47-54
# lines [47, 49, 50, 51, 52, 53, 54]
# branches []

import pytest
from ansible.plugins.filter.core import to_yaml, AnsibleFilterError
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.module_utils._text import to_text, to_native
import yaml

def test_to_yaml(mocker):
    # Test with default_flow_style set to None
    data = {'key': 'value'}
    result = to_yaml(data)
    assert result == to_text(yaml.dump(data, Dumper=AnsibleDumper, allow_unicode=True, default_flow_style=None))

    # Test with default_flow_style set to True
    result = to_yaml(data, default_flow_style=True)
    assert result == to_text(yaml.dump(data, Dumper=AnsibleDumper, allow_unicode=True, default_flow_style=True))

    # Test with default_flow_style set to False
    result = to_yaml(data, default_flow_style=False)
    assert result == to_text(yaml.dump(data, Dumper=AnsibleDumper, allow_unicode=True, default_flow_style=False))

    # Test exception handling
    mocker.patch('yaml.dump', side_effect=Exception('test exception'))
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_yaml(data)
    assert 'to_yaml - test exception' in str(excinfo.value)
