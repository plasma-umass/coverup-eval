# file lib/ansible/utils/vars.py:58-79
# lines [58, 70, 71, 72, 73, 74, 75, 76, 77, 78]
# branches ['70->exit', '70->71', '72->73', '72->77']

import pytest
from ansible.errors import AnsibleError
from ansible.utils.vars import _validate_mutable_mappings
from collections.abc import MutableMapping

def test_validate_mutable_mappings_with_non_dicts():
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings([], {})
    assert "failed to combine variables, expected dicts but got a 'list' and a 'dict'" in str(excinfo.value)

    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings({}, [])
    assert "failed to combine variables, expected dicts but got a 'dict' and a 'list'" in str(excinfo.value)

    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings([], [])
    assert "failed to combine variables, expected dicts but got a 'list' and a 'list'" in str(excinfo.value)

def test_validate_mutable_mappings_with_dicts():
    try:
        _validate_mutable_mappings({}, {})
    except AnsibleError:
        pytest.fail("AnsibleError raised unexpectedly!")

@pytest.fixture(autouse=True)
def cleanup(mocker):
    mocker.stopall()
    yield
    mocker.stopall()
