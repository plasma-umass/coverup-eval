# file lib/ansible/plugins/lookup/sequence.py:173-206
# lines [173, 175, 176, 177, 179, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 197, 198, 199, 200, 201, 202, 203, 204, 206]
# branches ['176->177', '176->179', '181->182', '181->186', '186->187', '186->191', '191->192', '191->197', '197->198', '197->199', '199->200', '199->201', '201->202', '201->203', '203->204', '203->206']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

# Assuming SHORTCUT is a regex pattern defined in the module that we are testing
# If it's not defined, we would need to mock it or define it for the test

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_parse_simple_args_valid(lookup_module):
    assert lookup_module.parse_simple_args('1-10/2') is True
    assert lookup_module.start == 1
    assert lookup_module.end == 10
    assert lookup_module.stride == 2

def test_parse_simple_args_invalid_start(lookup_module):
    with pytest.raises(AnsibleError) as excinfo:
        lookup_module.parse_simple_args('a-10/2')
    assert "can't parse start=a as integer" in str(excinfo.value)

def test_parse_simple_args_invalid_end(lookup_module):
    with pytest.raises(AnsibleError) as excinfo:
        lookup_module.parse_simple_args('1-b/2')
    assert "can't parse end=b as integer" in str(excinfo.value)

def test_parse_simple_args_invalid_stride(lookup_module):
    with pytest.raises(AnsibleError) as excinfo:
        lookup_module.parse_simple_args('1-10/c')
    assert "can't parse stride=c as integer" in str(excinfo.value)

def test_parse_simple_args_no_match(lookup_module):
    assert lookup_module.parse_simple_args('invalid') is False
