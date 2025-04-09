# file lib/ansible/playbook/base.py:792-815
# lines [801]
# branches ['800->801']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleAssertionError

class TestFieldAttributeBase(FieldAttributeBase):
    pass

def test_deserialize_raises_exception_with_non_dict_data(mocker):
    mocker.patch.object(TestFieldAttributeBase, '_valid_attrs', return_value={})
    test_instance = TestFieldAttributeBase()

    with pytest.raises(AnsibleAssertionError) as excinfo:
        test_instance.deserialize("not_a_dict")

    assert "data (not_a_dict) should be a dict but is a" in str(excinfo.value)
