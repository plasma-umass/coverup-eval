# file: lib/ansible/playbook/base.py:518-527
# asked: {"lines": [518, 524, 525, 526, 527], "branches": [[524, 0], [524, 525], [525, 526], [525, 527]]}
# gained: {"lines": [518, 524, 525, 526, 527], "branches": [[524, 525], [525, 526], [525, 527]]}

import pytest
from unittest.mock import MagicMock

from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def field_attribute_base():
    instance = FieldAttributeBase()
    instance._valid_attrs = {'attr1': 'value1', 'attr2': 'value2'}
    instance._attributes = {}
    return instance

def test_squash(field_attribute_base):
    instance = field_attribute_base
    instance.attr1 = 'evaluated_attr1'
    instance.attr2 = 'evaluated_attr2'
    
    assert not instance._squashed
    instance.squash()
    assert instance._squashed
    assert instance._attributes['attr1'] == 'evaluated_attr1'
    assert instance._attributes['attr2'] == 'evaluated_attr2'
