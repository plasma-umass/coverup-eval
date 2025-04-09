# file lib/ansible/playbook/base.py:322-347
# lines [322, 324, 326, 328, 330, 331, 334, 335, 336, 339, 340, 341, 342, 343, 344, 347]
# branches ['326->328', '326->347', '328->330', '328->347', '330->331', '330->334', '335->336', '335->339', '340->328', '340->341', '341->328', '341->342']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

class MockAttribute:
    def __init__(self, isa):
        self.isa = isa

class MockFieldAttributeBase(FieldAttributeBase):
    def __init__(self):
        self._validated = False
        self._valid_attrs = {
            'test_string': MockAttribute('string'),
            'test_list': MockAttribute('string')
        }
        self._alias_attrs = {}
        self._attributes = {
            'test_string': 'valid_string',
            'test_list': 'valid_string'
        }

    def get_ds(self):
        return {}

def test_validate_string_type():
    obj = MockFieldAttributeBase()
    
    # This should pass without exceptions
    obj.validate()
    assert obj._validated is True

    # Reset validation state
    obj._validated = False
    obj._attributes['test_string'] = ['invalid', 'list']
    
    # This should raise an AnsibleParserError
    with pytest.raises(AnsibleParserError, match="The field 'test_string' is supposed to be a string type, however the incoming data structure is a <class 'list'>"):
        obj.validate()

    # Reset validation state
    obj._validated = False
    obj._attributes['test_string'] = 'valid_string'
    obj._attributes['test_list'] = ['invalid', 'list']
    
    # This should raise an AnsibleParserError
    with pytest.raises(AnsibleParserError, match="The field 'test_list' is supposed to be a string type, however the incoming data structure is a <class 'list'>"):
        obj.validate()

    # Reset validation state
    obj._validated = False
    obj._attributes['test_list'] = 'valid_string'
    
    # This should pass without exceptions
    obj.validate()
    assert obj._validated is True
