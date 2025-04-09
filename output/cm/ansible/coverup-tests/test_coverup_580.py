# file lib/ansible/plugins/filter/core.py:57-63
# lines [57, 59, 60, 61, 62, 63]
# branches []

import pytest
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_native, to_text
from ansible.plugins.filter.core import to_nice_yaml
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml

def test_to_nice_yaml_exception(mocker):
    # Mock yaml.dump to raise an exception
    mocker.patch('yaml.dump', side_effect=Exception('test exception'))
    
    # Mock AnsibleDumper just in case it's needed
    mocker.patch('ansible.parsing.yaml.dumper.AnsibleDumper')
    
    # Test that to_nice_yaml raises the correct exception when yaml.dump fails
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_nice_yaml({'key': 'value'})
    assert "to_nice_yaml - test exception" in str(excinfo.value)
