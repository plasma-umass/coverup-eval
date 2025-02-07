# file: lib/ansible/playbook/base.py:304-309
# asked: {"lines": [304, 305, 306, 307, 308, 309], "branches": [[307, 308], [307, 309]]}
# gained: {"lines": [304, 305, 306, 307, 308, 309], "branches": [[307, 308], [307, 309]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types

class MockTemplar:
    def template(self, value):
        return value

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_post_validate_debugger_valid_value(field_attribute_base):
    templar = MockTemplar()
    valid_values = ['always', 'on_failed', 'on_unreachable', 'on_skipped', 'never']
    for value in valid_values:
        assert field_attribute_base._post_validate_debugger('debugger', value, templar) == value

def test_post_validate_debugger_invalid_value(field_attribute_base):
    templar = MockTemplar()
    invalid_value = 'invalid_value'
    with pytest.raises(AnsibleParserError, match="'%s' is not a valid value for debugger. Must be one of on_unreachable, always, on_skipped, on_failed, never" % invalid_value):
        field_attribute_base._post_validate_debugger('debugger', invalid_value, templar)

def test_post_validate_debugger_non_string_value(field_attribute_base):
    templar = MockTemplar()
    non_string_value = 12345
    assert field_attribute_base._post_validate_debugger('debugger', non_string_value, templar) == non_string_value
