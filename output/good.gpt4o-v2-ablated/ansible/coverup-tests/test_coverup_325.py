# file: lib/ansible/playbook/base.py:243-245
# asked: {"lines": [243, 245], "branches": []}
# gained: {"lines": [243, 245], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

def test_preprocess_data():
    instance = FieldAttributeBase()
    data = {"key": "value"}
    result = instance.preprocess_data(data)
    assert result == data
