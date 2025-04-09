# file: lib/ansible/plugins/lookup/sequence.py:229-243
# asked: {"lines": [229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242], "branches": [[230, 231], [230, 233], [236, 0], [236, 237]]}
# gained: {"lines": [229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242], "branches": [[230, 231], [230, 233], [236, 0], [236, 237]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

class MockLookupModule(LookupModule):
    def __init__(self, start, end, stride, format):
        self.start = start
        self.end = end
        self.stride = stride
        self.format = format

@pytest.fixture
def mock_lookup_module():
    return MockLookupModule(1, 5, 1, "%d")

def test_generate_sequence_positive_stride(mock_lookup_module):
    mock_lookup_module.stride = 1
    result = list(mock_lookup_module.generate_sequence())
    assert result == ["1", "2", "3", "4", "5"]

def test_generate_sequence_negative_stride():
    mock_module = MockLookupModule(5, 1, -1, "%d")
    result = list(mock_module.generate_sequence())
    assert result == ["5", "4", "3", "2", "1"]

def test_generate_sequence_formatting_error():
    mock_module = MockLookupModule(1, 5, 1, "%d %d")
    with pytest.raises(AnsibleError, match="problem formatting"):
        list(mock_module.generate_sequence())

def test_generate_sequence_type_error():
    mock_module = MockLookupModule(1, 5, 1, "%d")
    mock_module.format = None  # This will cause a TypeError
    with pytest.raises(AnsibleError, match="problem formatting"):
        list(mock_module.generate_sequence())
