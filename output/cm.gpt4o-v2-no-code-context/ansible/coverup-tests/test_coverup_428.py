# file: lib/ansible/playbook/base.py:304-309
# asked: {"lines": [304, 305, 306, 307, 308, 309], "branches": [[307, 308], [307, 309]]}
# gained: {"lines": [304, 305, 306, 307, 308, 309], "branches": [[307, 308], [307, 309]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.template import Templar
from ansible.utils.vars import load_extra_vars

class MockTemplar:
    def template(self, value):
        return value

class MockFieldAttributeBase(FieldAttributeBase):
    def get_ds(self):
        return {}

@pytest.fixture
def mock_templar():
    return MockTemplar()

@pytest.fixture
def field_attribute_base():
    return MockFieldAttributeBase()

def test_post_validate_debugger_valid_value(field_attribute_base, mock_templar):
    valid_values = ['always', 'on_failed', 'on_unreachable', 'on_skipped', 'never']
    for value in valid_values:
        assert field_attribute_base._post_validate_debugger('debugger', value, mock_templar) == value

def test_post_validate_debugger_invalid_value(field_attribute_base, mock_templar):
    invalid_value = 'invalid_value'
    with pytest.raises(AnsibleParserError) as excinfo:
        field_attribute_base._post_validate_debugger('debugger', invalid_value, mock_templar)
    assert "'invalid_value' is not a valid value for debugger" in str(excinfo.value)

def test_post_validate_debugger_non_string_value(field_attribute_base, mock_templar):
    non_string_value = 12345
    assert field_attribute_base._post_validate_debugger('debugger', non_string_value, mock_templar) == non_string_value
