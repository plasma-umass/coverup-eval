# file: lib/ansible/playbook/base.py:225-227
# asked: {"lines": [225, 226, 227], "branches": []}
# gained: {"lines": [225, 226, 227], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

def test_finalized_property():
    instance = FieldAttributeBase()
    assert not instance.finalized  # Check the default value

    instance._finalized = True
    assert instance.finalized  # Check the updated value
