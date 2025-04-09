# file lib/ansible/plugins/lookup/sequence.py:229-243
# lines [229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242]
# branches ['230->231', '230->233', '236->exit', '236->237']

import pytest
from ansible.plugins.lookup.sequence import LookupModule
from ansible.errors import AnsibleError

class MockLookupBase:
    pass

@pytest.fixture
def mock_lookup_module(mocker):
    mocker.patch('ansible.plugins.lookup.sequence.LookupBase', MockLookupBase)
    return LookupModule()

def test_generate_sequence_positive_stride(mock_lookup_module):
    mock_lookup_module.start = 1
    mock_lookup_module.end = 5
    mock_lookup_module.stride = 1
    mock_lookup_module.format = "%d"
    
    result = list(mock_lookup_module.generate_sequence())
    assert result == ['1', '2', '3', '4', '5']

def test_generate_sequence_negative_stride(mock_lookup_module):
    mock_lookup_module.start = 5
    mock_lookup_module.end = 1
    mock_lookup_module.stride = -1
    mock_lookup_module.format = "%d"
    
    result = list(mock_lookup_module.generate_sequence())
    assert result == ['5', '4', '3', '2', '1']

def test_generate_sequence_format_error(mock_lookup_module):
    mock_lookup_module.start = 1
    mock_lookup_module.end = 5
    mock_lookup_module.stride = 1
    mock_lookup_module.format = "%d %d"
    
    with pytest.raises(AnsibleError, match="problem formatting"):
        list(mock_lookup_module.generate_sequence())
