# file lib/ansible/playbook/base.py:304-309
# lines [304, 305, 306, 307, 308, 309]
# branches ['307->308', '307->309']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils.six import string_types

class MockTemplar:
    def template(self, value):
        return value

@pytest.fixture
def field_attribute_base():
    class TestFieldAttributeBase(FieldAttributeBase):
        def get_ds(self):
            return {}
    return TestFieldAttributeBase()

def test_post_validate_debugger_valid_value(field_attribute_base):
    templar = MockTemplar()
    valid_values = ['always', 'on_failed', 'on_unreachable', 'on_skipped', 'never']
    for value in valid_values:
        assert field_attribute_base._post_validate_debugger('debugger', value, templar) == value

def test_post_validate_debugger_invalid_value(field_attribute_base):
    templar = MockTemplar()
    invalid_value = 'invalid_value'
    with pytest.raises(AnsibleParserError) as excinfo:
        field_attribute_base._post_validate_debugger('debugger', invalid_value, templar)
    assert "'invalid_value' is not a valid value for debugger" in str(excinfo.value)

def test_post_validate_debugger_templated_value(field_attribute_base, mocker):
    templar = mocker.Mock(spec=Templar)
    templar.template.return_value = 'always'
    assert field_attribute_base._post_validate_debugger('debugger', 'always', templar) == 'always'
    templar.template.assert_called_once_with('always')
