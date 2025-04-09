# file lib/ansible/playbook/base.py:518-527
# lines [524, 525, 526, 527]
# branches ['524->exit', '524->525', '525->526', '525->527']

import pytest
from ansible.playbook.base import FieldAttributeBase

class MockFieldAttributeBase(FieldAttributeBase):
    _valid_attrs = {
        'test_attr': None
    }

    def __init__(self):
        super(MockFieldAttributeBase, self).__init__()
        self._squashed = False
        self._attributes = {'test_attr': 'initial_value'}

    @property
    def test_attr(self):
        return self._attributes.get('test_attr')

@pytest.fixture
def mock_field_attribute_base():
    return MockFieldAttributeBase()

def test_squash(mock_field_attribute_base):
    # Precondition: _squashed is False and test_attr has its initial value
    assert not mock_field_attribute_base._squashed
    assert mock_field_attribute_base.test_attr == 'initial_value'

    # Action: Call the squash method
    mock_field_attribute_base.squash()

    # Postconditions: _squashed is True and test_attr is still accessible with the same value
    assert mock_field_attribute_base._squashed
    assert mock_field_attribute_base.test_attr == 'initial_value'
