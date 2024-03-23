# file lib/ansible/plugins/filter/core.py:47-54
# lines [47, 49, 50, 51, 52, 53, 54]
# branches []

import pytest
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_native, to_text
from ansible.parsing.yaml.dumper import AnsibleDumper
import yaml

# Assuming the to_yaml function is part of a class named FilterModule in core.py
# and that the function is a standalone function, not a method of FilterModule.
from ansible.plugins.filter.core import to_yaml

def test_to_yaml_exception_handling(mocker):
    # Mock yaml.dump to raise an exception
    mocker.patch('yaml.dump', side_effect=Exception("test exception"))

    # Test that to_yaml raises AnsibleFilterError when yaml.dump raises an Exception
    with pytest.raises(AnsibleFilterError) as excinfo:
        to_yaml({'key': 'value'})
    assert "to_yaml - test exception" in str(excinfo.value)

    # Cleanup is handled by pytest-mock through the mocker fixture
