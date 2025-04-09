# file lib/ansible/utils/vars.py:58-79
# lines [58, 70, 71, 72, 73, 74, 75, 76, 77, 78]
# branches ['70->exit', '70->71', '72->73', '72->77']

import pytest
from ansible.errors import AnsibleError
from collections.abc import MutableMapping
from ansible.parsing.ajson import AnsibleJSONEncoder
from ansible.module_utils._text import to_native
import json

# Assuming the above code is part of a module named `ansible.utils.vars`
# and the function `_validate_mutable_mappings` is importable for testing purposes
from ansible.utils.vars import _validate_mutable_mappings

def dumps(data):
    return json.dumps(data, cls=AnsibleJSONEncoder)

@pytest.fixture
def non_mapping_objects():
    class NonMapping:
        pass

    return NonMapping(), NonMapping()

def test_validate_mutable_mappings_with_non_mappings(non_mapping_objects, mocker):
    a, b = non_mapping_objects
    mocker.patch('ansible.utils.vars.dumps', side_effect=Exception("Mocked exception for non-serializable object"))
    mocker.patch('ansible.utils.vars.to_native', return_value="NonMappingType")

    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)

    assert "expected dicts but got a 'NonMapping' and a 'NonMapping'" in str(excinfo.value)
    assert "NonMappingType" in str(excinfo.value)
