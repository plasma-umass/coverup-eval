# file lib/ansible/playbook/play.py:104-119
# lines []
# branches ['106->exit']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.module_utils._text import to_bytes, to_text

# Mocking the Base and CollectionSearch classes since they are not provided
class Base:
    def __init__(self, *args, **kwargs):
        self._ds = {}

class CollectionSearch:
    def __init__(self, *args, **kwargs):
        pass

# Define the test function
def test_play_validate_hosts_with_invalid_host_value():
    play = Play()

    # Set the _ds attribute to include 'hosts'
    play._ds = {'hosts': True}

    # Test with an empty hosts list
    with pytest.raises(AnsibleParserError) as excinfo:
        play._validate_hosts('hosts', 'hosts', [])
    assert "Hosts list cannot be empty" in str(excinfo.value)

    # Test with an invalid host value in the list
    with pytest.raises(AnsibleParserError) as excinfo:
        play._validate_hosts('hosts', 'hosts', [None])
    assert "Hosts list cannot contain values of 'None'" in str(excinfo.value)

    # Test with an invalid host value that is not a string
    with pytest.raises(AnsibleParserError) as excinfo:
        play._validate_hosts('hosts', 'hosts', [123])
    assert "Hosts list contains an invalid host value: '123'" in str(excinfo.value)

    # Test with an invalid host value that is not a sequence or string
    with pytest.raises(AnsibleParserError) as excinfo:
        play._validate_hosts('hosts', 'hosts', 123)
    assert "Hosts list must be a sequence or string" in str(excinfo.value)

    # Test with a valid binary_type host value
    try:
        play._validate_hosts('hosts', 'hosts', to_bytes('localhost'))
    except AnsibleParserError:
        pytest.fail("Unexpected AnsibleParserError with a valid binary_type host value")

    # Test with a valid text_type host value
    try:
        play._validate_hosts('hosts', 'hosts', to_text('localhost'))
    except AnsibleParserError:
        pytest.fail("Unexpected AnsibleParserError with a valid text_type host value")

    # Test with 'hosts' not in _ds to cover branch 106->exit
    play._ds = {}
    try:
        play._validate_hosts('hosts', 'hosts', 'localhost')
    except AnsibleParserError:
        pytest.fail("Unexpected AnsibleParserError when 'hosts' not in _ds")
