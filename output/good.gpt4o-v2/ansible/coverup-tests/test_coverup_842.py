# file: lib/ansible/playbook/base.py:298-299
# asked: {"lines": [298, 299], "branches": []}
# gained: {"lines": [298, 299], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

def test_get_loader():
    instance = FieldAttributeBase()
    instance._loader = "test_loader"
    assert instance.get_loader() == "test_loader"
