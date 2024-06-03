# file lib/ansible/plugins/filter/core.py:57-63
# lines [57, 59, 60, 61, 62, 63]
# branches []

import pytest
from ansible.plugins.filter.core import to_nice_yaml, AnsibleFilterError, AnsibleDumper
from ansible.module_utils._text import to_text
import yaml

def test_to_nice_yaml(mocker):
    # Mocking to_native
    mocker.patch('ansible.plugins.filter.core.to_native', side_effect=lambda x: str(x))

    # Test with a simple dictionary
    data = {'key': 'value'}
    result = to_nice_yaml(data)
    expected_result = to_text(yaml.dump(data, Dumper=AnsibleDumper, indent=4, allow_unicode=True, default_flow_style=False))
    assert result == expected_result

    # Test with an exception
    mocker.patch('yaml.dump', side_effect=Exception('test exception'))
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_nice_yaml(data)
    assert 'to_nice_yaml - test exception' in str(excinfo.value)
