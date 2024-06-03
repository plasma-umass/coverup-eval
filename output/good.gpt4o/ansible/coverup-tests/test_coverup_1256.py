# file lib/ansible/playbook/base.py:792-815
# lines [801]
# branches ['800->801']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleAssertionError

def test_deserialize_with_non_dict_data():
    class TestFieldAttributeBase(FieldAttributeBase):
        _valid_attrs = {}

    obj = TestFieldAttributeBase()
    
    with pytest.raises(AnsibleAssertionError) as excinfo:
        obj.deserialize("not_a_dict")
    
    assert str(excinfo.value) == "data (not_a_dict) should be a dict but is a <class 'str'>"
