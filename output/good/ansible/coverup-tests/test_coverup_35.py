# file lib/ansible/plugins/filter/core.py:489-532
# lines [489, 498, 499, 500, 501, 503, 505, 506, 507, 508, 510, 512, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 529, 530, 532]
# branches ['498->499', '498->500', '500->501', '500->503', '505->506', '505->507', '507->508', '507->510', '514->515', '514->532', '516->517', '516->526', '520->521', '520->523', '526->527', '526->529', '529->514', '529->530']

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError

# Assuming the subelements function is part of a module named ansible.plugins.filter.core
from ansible.plugins.filter.core import subelements

def test_subelements_with_nested_dict_and_skip_missing(mocker):
    # Setup
    obj = {"name": "alice", "details": {"groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}}
    subelement_path = 'details.groups'
    expected = [({'name': 'alice', 'details': {'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}}, 'wheel')]

    # Exercise
    result = subelements([obj], subelement_path, skip_missing=True)  # Pass a list of dicts instead of a dict

    # Verify
    assert result == expected

    # Cleanup - nothing to clean up as we did not modify any global state

def test_subelements_with_missing_key_and_skip_missing(mocker):
    # Setup
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    subelement_path = 'nonexistent.key'
    expected = []

    # Exercise
    result = subelements(obj, subelement_path, skip_missing=True)

    # Verify
    assert result == expected

    # Cleanup - nothing to clean up as we did not modify any global state

def test_subelements_with_missing_key_and_not_skip_missing(mocker):
    # Setup
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    subelement_path = 'nonexistent.key'

    # Exercise and Verify
    with pytest.raises(AnsibleFilterError):
        subelements(obj, subelement_path, skip_missing=False)

    # Cleanup - nothing to clean up as we did not modify any global state

def test_subelements_with_incorrect_type_for_values(mocker):
    # Setup
    obj = [{"name": "alice", "groups": "wheel", "authorized": ["/tmp/alice/onekey.pub"]}]
    subelement_path = 'groups'

    # Exercise and Verify
    with pytest.raises(AnsibleFilterTypeError):
        subelements(obj, subelement_path)

    # Cleanup - nothing to clean up as we did not modify any global state

def test_subelements_with_incorrect_type_for_subelements(mocker):
    # Setup
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    subelement_path = 123  # Incorrect type

    # Exercise and Verify
    with pytest.raises(AnsibleFilterTypeError):
        subelements(obj, subelement_path)

    # Cleanup - nothing to clean up as we did not modify any global state
