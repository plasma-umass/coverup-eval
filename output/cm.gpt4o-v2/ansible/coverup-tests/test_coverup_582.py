# file: lib/ansible/plugins/filter/core.py:57-63
# asked: {"lines": [57, 59, 60, 61, 62, 63], "branches": []}
# gained: {"lines": [57, 59, 60, 61, 62, 63], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_native, to_text
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml

from ansible.plugins.filter.core import to_nice_yaml

def test_to_nice_yaml_success():
    data = {'key': 'value'}
    result = to_nice_yaml(data)
    assert isinstance(result, str)
    assert 'key' in result
    assert 'value' in result

def test_to_nice_yaml_exception(mocker):
    data = {'key': 'value'}
    mocker.patch('yaml.dump', side_effect=Exception('test exception'))
    
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_nice_yaml(data)
    
    assert 'to_nice_yaml - test exception' in str(excinfo.value)
    assert excinfo.value.orig_exc is not None
    assert isinstance(excinfo.value.orig_exc, Exception)
