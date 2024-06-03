# file lib/ansible/parsing/mod_args.py:140-193
# lines [155]
# branches ['154->155']

import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleParserError
from ansible.template import Templar
from ansible.utils.unicode import to_text

class MockTemplar:
    def __init__(self, loader=None):
        pass

    def is_template(self, var):
        return True

@pytest.fixture
def mock_templar(mocker):
    mocker.patch('ansible.parsing.mod_args.Templar', MockTemplar)

def test_normalize_parameters_with_template_string(mock_templar):
    parser = ModuleArgsParser()
    thing = {}
    action = None
    additional_args = "{{ var_name }}"
    
    action, final_args = parser._normalize_parameters(thing, action, additional_args)
    
    assert '_variable_params' in final_args
    assert final_args['_variable_params'] == additional_args
