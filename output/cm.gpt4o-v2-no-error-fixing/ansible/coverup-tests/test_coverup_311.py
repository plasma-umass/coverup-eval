# file: lib/ansible/playbook/base.py:518-527
# asked: {"lines": [518, 524, 525, 526, 527], "branches": [[524, 0], [524, 525], [525, 526], [525, 527]]}
# gained: {"lines": [518, 524, 525, 526, 527], "branches": [[524, 0], [524, 525], [525, 526], [525, 527]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def field_attribute_base():
    from ansible.playbook.base import FieldAttributeBase
    fab = FieldAttributeBase()
    fab._valid_attrs = {'attr1': 'value1', 'attr2': 'value2'}
    fab._attributes = {}
    fab._squashed = False
    return fab

def test_squash(field_attribute_base):
    fab = field_attribute_base
    fab.attr1 = 'evaluated_value1'
    fab.attr2 = 'evaluated_value2'
    
    fab.squash()
    
    assert fab._attributes['attr1'] == 'evaluated_value1'
    assert fab._attributes['attr2'] == 'evaluated_value2'
    assert fab._squashed is True

    # Ensure squash does not run again
    fab._attributes['attr1'] = 'changed_value'
    fab.squash()
    assert fab._attributes['attr1'] == 'changed_value'
